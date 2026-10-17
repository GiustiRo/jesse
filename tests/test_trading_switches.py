from pathlib import Path

from jesse_live import switches


def test_missing_file_defaults_to_armed_and_trading(tmp_path, monkeypatch):
    monkeypatch.setenv("JESSE_ENV_FILE", str(tmp_path / ".env"))
    (tmp_path / ".env").write_text("PASSWORD=x\n", encoding="utf-8")
    assert switches.load_switches() == {"armed": True, "allow_trading": True}


def test_save_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setenv("JESSE_ENV_FILE", str(tmp_path / ".env"))
    (tmp_path / ".env").write_text("PASSWORD=x\n", encoding="utf-8")
    saved = switches.save_switches(armed=False, allow_trading=True)
    assert saved == {"armed": False, "allow_trading": True}
    assert switches.is_armed() is False
    assert switches.allow_trading() is True
    path = Path(tmp_path) / "storage" / "trading_switches.json"
    assert path.exists()
    switches.save_switches(allow_trading=False)
    assert switches.load_switches() == {"armed": False, "allow_trading": False}


def test_corrupt_file_falls_back_to_defaults(tmp_path, monkeypatch):
    monkeypatch.setenv("JESSE_ENV_FILE", str(tmp_path / ".env"))
    storage = tmp_path / "storage"
    storage.mkdir()
    (storage / "trading_switches.json").write_text("{not json", encoding="utf-8")
    assert switches.load_switches() == {"armed": True, "allow_trading": True}
