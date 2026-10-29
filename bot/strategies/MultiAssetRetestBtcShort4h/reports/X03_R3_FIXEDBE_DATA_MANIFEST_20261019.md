# FixedBE persistent complete data manifest

83 artifacts readtruncatedfalse and persistentlysavedviaMCP. Individual report JSON codefence wraps originalartifact content; sourceartifactSHA256appliestooriginalJSONpayload. Dynamicpartition manifests include rowcounts/canonical-fullrowsSHA256/concatenated-partbytesSHA256. Allparts<=35kB,summaries<=40kB. No inference frominitialtruncatedartifact.

```json
{
  "output_manifest": {
    "artifacts": [
      {
        "path": "FBS0B_BTC_USDT_2021_changes_part1.json",
        "size_bytes": 1195,
        "sha256": "ce7c37beb8e455d34a4bb805bed989904110a0485ef007b3847049353a375c17"
      },
      {
        "path": "FBS0B_BTC_USDT_2022_changes_part1.json",
        "size_bytes": 2606,
        "sha256": "57bb59f62f8768c3a48a1ebedf4b8e4b51cf761be36e0249170bd6ac7a2a28f4"
      },
      {
        "path": "FBS0B_BTC_USDT_2023_changes_part1.json",
        "size_bytes": 10139,
        "sha256": "d65303c366d2cc118bed6d22c316aae19d25ed15033794ce8b250e02c18501c1"
      },
      {
        "path": "FBS0B_BTC_USDT_2024_changes_part1.json",
        "size_bytes": 8944,
        "sha256": "f2e73bb65d1da11da25fb8638d8a163cce382a65d5b37fac08bcd57f120e8e60"
      },
      {
        "path": "FBS0B_BTC_USDT_2025_changes_part1.json",
        "size_bytes": 33977,
        "sha256": "b498c6043fd4f5996cc47a4fb54a9c5e31f0841b39ce49787fdb35d33a144bb8"
      },
      {
        "path": "FBS0B_BTC_USDT_2025_changes_part2.json",
        "size_bytes": 10049,
        "sha256": "2b2fb364d4e4b0b89bcdc010e1cc98914f44354398b887038f640ce5acd5ff4a"
      },
      {
        "path": "FBS0B_BTC_USDT_stop_endpoints_part1.json",
        "size_bytes": 19478,
        "sha256": "6800202a72a5103afa3cfbf2a0f1e87d5a51fc7a3668c09c0044b3630b573083"
      },
      {
        "path": "FBS0B_PAXG_USDT_2020_changes_part1.json",
        "size_bytes": 1308,
        "sha256": "66d64184859e6dae22ecef5467ae47cf9e1eb1c44b580629bed808a9e8f9fa34"
      },
      {
        "path": "FBS0B_PAXG_USDT_2021_changes_part1.json",
        "size_bytes": 6298,
        "sha256": "52f85c80534170c30ede54ee49911bc9ae87f32e75405aa71a544288b5caf716"
      },
      {
        "path": "FBS0B_PAXG_USDT_2022_changes_part1.json",
        "size_bytes": 3776,
        "sha256": "a3c2b5829c45ba0f705ed68bbc83fec4c699d45b5d991679ca28257486a5139d"
      },
      {
        "path": "FBS0B_PAXG_USDT_2023_changes_part1.json",
        "size_bytes": 8774,
        "sha256": "ac5b9c8d8b65af44576fb6932751524f843747d4ae5f5c6f202c100a069d1eed"
      },
      {
        "path": "FBS0B_PAXG_USDT_2024_changes_part1.json",
        "size_bytes": 8664,
        "sha256": "b735e0fb1e15bc86a0681dcb3df30063ade055b88a3196599c64893cc28151fc"
      },
      {
        "path": "FBS0B_PAXG_USDT_2025_changes_part1.json",
        "size_bytes": 19927,
        "sha256": "ba89e4372e4aa24e04301e9a3ea793fb4b77f4c91a215b2fe05115a8d4b51179"
      },
      {
        "path": "FBS0B_PAXG_USDT_stop_endpoints_part1.json",
        "size_bytes": 30113,
        "sha256": "2bbd8323e1dfb881e8a70cf77c0e9ce214b597d6a425e8c97ea98a3ce24eceb1"
      },
      {
        "path": "FBS0B_SPY_USDT_2021_changes_part1.json",
        "size_bytes": 1224,
        "sha256": "b3be084d613d90bbd4568b05af04c1ed97b413a6330497dcf389d5193ee9aede"
      },
      {
        "path": "FBS0B_SPY_USDT_2022_changes_part1.json",
        "size_bytes": 1223,
        "sha256": "c889a2e6511c4b145ed37ad1b0518fb3c50dcabbb6042f7249909d69179655cd"
      },
      {
        "path": "FBS0B_SPY_USDT_2023_changes_part1.json",
        "size_bytes": 4931,
        "sha256": "e4cb06222bbc517c2f2825f59167498be0fbc3ee96a459ccb2b3b949c8063a92"
      },
      {
        "path": "FBS0B_SPY_USDT_2024_changes_part1.json",
        "size_bytes": 3664,
        "sha256": "6c8ac444a55df461ce5b4a26ccaa000bf62ffc38492002600b378bcc2815ccc8"
      },
      {
        "path": "FBS0B_SPY_USDT_2025_changes_part1.json",
        "size_bytes": 2573,
        "sha256": "248d109abd68b0f8ef9c6906aee1157c9161fa2892ac39a31cab379031e17a95"
      },
      {
        "path": "FBS0B_SPY_USDT_stop_endpoints_part1.json",
        "size_bytes": 8602,
        "sha256": "d090de974b8d3d07d2af399742bb8282c4c1b9e710336b1614a127115c8795c9"
      },
      {
        "path": "FBS0B_divergence_summary.json",
        "size_bytes": 15239,
        "sha256": "50f3bc8cb1745bc6a0a78be9be4cae7cbd2e4ded15df6617ea7f1ee21d9a4d6b"
      },
      {
        "path": "FBS0C_BTC_USDT_2021_changes_part1.json",
        "size_bytes": 6268,
        "sha256": "6fd2a7f2850c337ae1a0ea1223ad0c692121769b2d944a70d135004f15b9fc24"
      },
      {
        "path": "FBS0C_BTC_USDT_2022_changes_part1.json",
        "size_bytes": 14964,
        "sha256": "0ad7a573baaead70085f95741709e2005ae13987aa30663c015f7bfb00f5553c"
      },
      {
        "path": "FBS0C_BTC_USDT_2023_changes_part1.json",
        "size_bytes": 30534,
        "sha256": "782cd9e30884a68c1e217d700448d1799b97499e1b9763998f67e7677ef775e3"
      },
      {
        "path": "FBS0C_BTC_USDT_2024_changes_part1.json",
        "size_bytes": 17406,
        "sha256": "f1a05ac5717dc9b74ee749b90d63cd32cada301874208ae3e8dc6aebbe904437"
      },
      {
        "path": "FBS0C_BTC_USDT_2025_changes_part1.json",
        "size_bytes": 33841,
        "sha256": "f7d3ca0d9eb5fdec7a487bc2c3480df44ce9eac8ebad60413ced5b753aa165a5"
      },
      {
        "path": "FBS0C_BTC_USDT_2025_changes_part2.json",
        "size_bytes": 11304,
        "sha256": "1c1ab4a403a9cad99887afd707ac07b87b552a262490afeaa80569549919d7cc"
      },
      {
        "path": "FBS0C_BTC_USDT_stop_endpoints_part1.json",
        "size_bytes": 26563,
        "sha256": "1e2eb1deec299bb733936e23cbd4f968386bdadacce166bde278fbef4e1a5be8"
      },
      {
        "path": "FBS0C_PAXG_USDT_2020_changes_part1.json",
        "size_bytes": 1314,
        "sha256": "85e1b6f337e7a3947ddcfae64e8e22e71041aa28ec35fa564ec78da2ceef2a85"
      },
      {
        "path": "FBS0C_PAXG_USDT_2021_changes_part1.json",
        "size_bytes": 6628,
        "sha256": "b6b10cc6a061674796cc830dc2214a9e25e42ed95ea21e52e30f716ee57b5441"
      },
      {
        "path": "FBS0C_PAXG_USDT_2022_changes_part1.json",
        "size_bytes": 3844,
        "sha256": "3bc90922082389dea0702a83ec11e9de05e4809b77214d13f3dfac19f25e70a2"
      },
      {
        "path": "FBS0C_PAXG_USDT_2023_changes_part1.json",
        "size_bytes": 9199,
        "sha256": "af2e5cb8fa41c05c00e937d16a386db18a29d9acd338193981ae4807a795a1e5"
      },
      {
        "path": "FBS0C_PAXG_USDT_2024_changes_part1.json",
        "size_bytes": 8767,
        "sha256": "4724d4f8ace9e828643fab737b1ea3e474319ea91241d983905534e858ea9f6c"
      },
      {
        "path": "FBS0C_PAXG_USDT_2025_changes_part1.json",
        "size_bytes": 19954,
        "sha256": "304f3dc6fc7f339d3b1f19025dd18097a2ff87df2803a426ef4536aa24bc07ff"
      },
      {
        "path": "FBS0C_PAXG_USDT_stop_endpoints_part1.json",
        "size_bytes": 30343,
        "sha256": "f427d0b6af66e66a5b00d29ff5f14ba8af228ce9cbb574c146ca54de2be4dcfb"
      },
      {
        "path": "FBS0C_SPY_USDT_2021_changes_part1.json",
        "size_bytes": 3926,
        "sha256": "382e8279be4ca8e0dfd426de06f224a36b90cdd9e4ca31ac5b0b6d9512b9e90e"
      },
      {
        "path": "FBS0C_SPY_USDT_2022_changes_part1.json",
        "size_bytes": 2507,
        "sha256": "4863ee58f35ff5001ffe824f45f9ca5704d49ccabe4c6192e3daaed9a38d0837"
      },
      {
        "path": "FBS0C_SPY_USDT_2023_changes_part1.json",
        "size_bytes": 7512,
        "sha256": "85a3fd8a336f198da8aa65b5bc1ce04e69a70a58558f550919ed115ddd5b5a07"
      },
      {
        "path": "FBS0C_SPY_USDT_2024_changes_part1.json",
        "size_bytes": 5008,
        "sha256": "d86d91932df7aded87a8a6079439872a59ffeecb324637dd2ead53589ed7cd3d"
      },
      {
        "path": "FBS0C_SPY_USDT_2025_changes_part1.json",
        "size_bytes": 3694,
        "sha256": "06a8b3ecf9aa6d9987501150994fe2866a56bb514bda2cceb79a5961db8a9d74"
      },
      {
        "path": "FBS0C_SPY_USDT_stop_endpoints_part1.json",
        "size_bytes": 13382,
        "sha256": "72a7f34fc570fad23645d3e6b0e037a5aa06514dbfd026aad60dbf4266786397"
      },
      {
        "path": "FBS0C_divergence_summary.json",
        "size_bytes": 15245,
        "sha256": "34a09fa733411e5aca31e4356dcd2e6e5242d81f4968bd03189f15daa6da925a"
      },
      {
        "path": "FBS1B_BTC_USDT_2022_changes_part1.json",
        "size_bytes": 2444,
        "sha256": "7f7671bb228e9731fee1af84a472ac46b3daec9250263d03e4a834ac93692cdc"
      },
      {
        "path": "FBS1B_BTC_USDT_2023_changes_part1.json",
        "size_bytes": 13690,
        "sha256": "45d7ca2ce42b1d4a3c664e7647e4bd0338ad740c60cd2d9290d43fbf38368c7f"
      },
      {
        "path": "FBS1B_BTC_USDT_2024_changes_part1.json",
        "size_bytes": 2424,
        "sha256": "d9631af63f7aee3fb541127549918eee9e00049ecfa90a0d68e1a14ba890865a"
      },
      {
        "path": "FBS1B_BTC_USDT_2025_changes_part1.json",
        "size_bytes": 34066,
        "sha256": "3dd9234c5f51bd1c4ae8a08bde39eeb67806895955cee373fb3913ae434cab58"
      },
      {
        "path": "FBS1B_BTC_USDT_2025_changes_part2.json",
        "size_bytes": 7470,
        "sha256": "0ce98aed1fcf19a468e0134c2a1092dc308f71b0b6b1edbf3d30272c74b93407"
      },
      {
        "path": "FBS1B_BTC_USDT_stop_endpoints_part1.json",
        "size_bytes": 14754,
        "sha256": "d24d6d15bb374feb23c51e9abc3c2135ea8c6fa6284f9e2d6f20faf31b43d6bd"
      },
      {
        "path": "FBS1B_PAXG_USDT_2020_changes_part1.json",
        "size_bytes": 1308,
        "sha256": "66d64184859e6dae22ecef5467ae47cf9e1eb1c44b580629bed808a9e8f9fa34"
      },
      {
        "path": "FBS1B_PAXG_USDT_2021_changes_part1.json",
        "size_bytes": 6443,
        "sha256": "21b86ed2f32a17dfd25987a5a7e36683bd4c4b4650aca4900d8a35e6cd0e134b"
      },
      {
        "path": "FBS1B_PAXG_USDT_2022_changes_part1.json",
        "size_bytes": 3961,
        "sha256": "c460d8977ebb5028097ca4ac2bcc13e45488ad3cdf0366a7f928753ffdf1cdbf"
      },
      {
        "path": "FBS1B_PAXG_USDT_2023_changes_part1.json",
        "size_bytes": 8722,
        "sha256": "9bfd4d27928a5163191c7b31e7985c2bf278b9fb1fce4fe3817713632085cb28"
      },
      {
        "path": "FBS1B_PAXG_USDT_2024_changes_part1.json",
        "size_bytes": 8648,
        "sha256": "81f29e2bf712fb2b3e59c8bff418ad8f2027dcb7c1e220bc62a3e6b19f313581"
      },
      {
        "path": "FBS1B_PAXG_USDT_2025_changes_part1.json",
        "size_bytes": 19755,
        "sha256": "4b0d4a07044250ccc5fd6ac90f81dfa3c974f2ac68c8383a0efab8d201f9b1e1"
      },
      {
        "path": "FBS1B_PAXG_USDT_stop_endpoints_part1.json",
        "size_bytes": 30005,
        "sha256": "02b6936dfc3d274a8ea042a1e3cae8e2406c10689382e80a890e35996bf97f9e"
      },
      {
        "path": "FBS1B_SPY_USDT_2021_changes_part1.json",
        "size_bytes": 1355,
        "sha256": "223e84f79366d369b9e7f6e2ae56572dd09ac4735467c5ac205ca6c31007b459"
      },
      {
        "path": "FBS1B_SPY_USDT_2022_changes_part1.json",
        "size_bytes": 1221,
        "sha256": "ce90f746b9e1d52362d11bdfa5f38304b5dfd534123ab265690177071508cc5a"
      },
      {
        "path": "FBS1B_SPY_USDT_2023_changes_part1.json",
        "size_bytes": 4937,
        "sha256": "fddcf6d388489437913fc437905f546783cd8988092ec21f26124b47d732d27b"
      },
      {
        "path": "FBS1B_SPY_USDT_2024_changes_part1.json",
        "size_bytes": 3667,
        "sha256": "7d05d68992e7f1fe8ee96eb42a94aac29ea426716ea51c218c461c08ce349124"
      },
      {
        "path": "FBS1B_SPY_USDT_2025_changes_part1.json",
        "size_bytes": 2647,
        "sha256": "f584b4bd0ced1a94bae5a2ecfc572f2b0b228a8ae68703762dcc0763291ccfeb"
      },
      {
        "path": "FBS1B_SPY_USDT_stop_endpoints_part1.json",
        "size_bytes": 8582,
        "sha256": "397589765786b539254b18b4d10d70719c382da15c2bb7df491158faa962c292"
      },
      {
        "path": "FBS1B_divergence_summary.json",
        "size_bytes": 14855,
        "sha256": "43a607c6c4675b2b95fe5f8cf6935787f7bafe27ae9bfef49f0b9462faa4623e"
      },
      {
        "path": "FBS1C_BTC_USDT_2022_changes_part1.json",
        "size_bytes": 1212,
        "sha256": "9dec974c41dffdca1c45dc9756a93853578634506b7cdfaec2c9505d6a37bcc8"
      },
      {
        "path": "FBS1C_BTC_USDT_2023_changes_part1.json",
        "size_bytes": 12267,
        "sha256": "739fcccc23356b1fe85a785f876710b918a85db0292ad85ec70eb94e7e0afafd"
      },
      {
        "path": "FBS1C_BTC_USDT_2024_changes_part1.json",
        "size_bytes": 7628,
        "sha256": "3abf85fc60e2f50039a4b8e31891388e19b7f41fd2c42251eab3e8e7446ee8f9"
      },
      {
        "path": "FBS1C_BTC_USDT_2025_changes_part1.json",
        "size_bytes": 33815,
        "sha256": "fe52e2701ff890208f2ba03e256a403ffe02874e783689b302313c40f557e5a3"
      },
      {
        "path": "FBS1C_BTC_USDT_2025_changes_part2.json",
        "size_bytes": 7707,
        "sha256": "f1cabecebbaefa545621860978142df28a450453ab44de7058d876b69058b4cf"
      },
      {
        "path": "FBS1C_BTC_USDT_stop_endpoints_part1.json",
        "size_bytes": 14834,
        "sha256": "672034f364b0b4c07bf489196f4f4668ee708e8e351f211b21c2838dccbad94c"
      },
      {
        "path": "FBS1C_PAXG_USDT_2020_changes_part1.json",
        "size_bytes": 1314,
        "sha256": "85e1b6f337e7a3947ddcfae64e8e22e71041aa28ec35fa564ec78da2ceef2a85"
      },
      {
        "path": "FBS1C_PAXG_USDT_2021_changes_part1.json",
        "size_bytes": 6295,
        "sha256": "366e2c6d75ddf8db718ec912515234c6bf995d9855034404d593e5a15d0316aa"
      },
      {
        "path": "FBS1C_PAXG_USDT_2022_changes_part1.json",
        "size_bytes": 3840,
        "sha256": "17f383f4290f737ecfe6f8f3a905cc03841332bb40397070a5f2b6f78e3f38fe"
      },
      {
        "path": "FBS1C_PAXG_USDT_2023_changes_part1.json",
        "size_bytes": 9315,
        "sha256": "02411a783b861d70591a913d12fdee20adcd33120c8663fbd850fb4804c02917"
      },
      {
        "path": "FBS1C_PAXG_USDT_2024_changes_part1.json",
        "size_bytes": 8841,
        "sha256": "7256d0435b8a5757c7eeb5d8b7a10a4ecc8536b97517e974cda43dad697a87b3"
      },
      {
        "path": "FBS1C_PAXG_USDT_2025_changes_part1.json",
        "size_bytes": 20109,
        "sha256": "93d6fb83121d08a9ca9e67f4bcd3cd1dc644d91d35c4f3c4ee9f14fbe10f1564"
      },
      {
        "path": "FBS1C_PAXG_USDT_stop_endpoints_part1.json",
        "size_bytes": 30255,
        "sha256": "2847f6a98ecfbc19187cd4b0b33b6861ad67601d284971ab7aecf45b5baf29c6"
      },
      {
        "path": "FBS1C_SPY_USDT_2021_changes_part1.json",
        "size_bytes": 4058,
        "sha256": "f2ed4b27cebc285eb9ff40d4bf0ca7a2a8c5865006c0612e18a89fff8f73dfc2"
      },
      {
        "path": "FBS1C_SPY_USDT_2022_changes_part1.json",
        "size_bytes": 2505,
        "sha256": "0ed466d5b3e55e528937163a76ce63ad9cf79d65b05d338b12f1541cfd33a693"
      },
      {
        "path": "FBS1C_SPY_USDT_2023_changes_part1.json",
        "size_bytes": 7716,
        "sha256": "63ae853ba20039bb679a0aa319e580a74d14df98bed249278a14e9a4b4c3dba7"
      },
      {
        "path": "FBS1C_SPY_USDT_2024_changes_part1.json",
        "size_bytes": 5005,
        "sha256": "6f391162041abf85f97cfc45a8b74e5b34b4044f2efe2e81418bad8291de72d8"
      },
      {
        "path": "FBS1C_SPY_USDT_2025_changes_part1.json",
        "size_bytes": 3699,
        "sha256": "618a4a29b019e4bb7093f6d71732e402d84b76cef49def42824d9058e97ec0af"
      },
      {
        "path": "FBS1C_SPY_USDT_stop_endpoints_part1.json",
        "size_bytes": 13460,
        "sha256": "55f5111f6ac6a5a2b2cc50cd58e38b332c4c59e9e155afcd43cc18efecda9576"
      },
      {
        "path": "FBS1C_divergence_summary.json",
        "size_bytes": 14891,
        "sha256": "cc0256c4e70fc5da0f8a5125b1d1118da4dc3d72ba61782780336d8802eedba3"
      },
      {
        "path": "fixedBE_implementation_contrasts.json",
        "size_bytes": 1125,
        "sha256": "7b6b5f7761d14408397fcc9268ee98da5c6cedfa550b1a50dfb48f54c4249862"
      }
    ],
    "total_artifacts": 83,
    "all_parts_max35000": true,
    "all_summaries_max40000": true
  },
  "persistent_reports": [
    {
      "artifact": "FBS0B_BTC_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_BTC_USDT_2021_changes_part1.md",
      "sha256": "ce7c37beb8e455d34a4bb805bed989904110a0485ef007b3847049353a375c17"
    },
    {
      "artifact": "FBS0B_BTC_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_BTC_USDT_2022_changes_part1.md",
      "sha256": "57bb59f62f8768c3a48a1ebedf4b8e4b51cf761be36e0249170bd6ac7a2a28f4"
    },
    {
      "artifact": "FBS0B_BTC_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_BTC_USDT_2023_changes_part1.md",
      "sha256": "d65303c366d2cc118bed6d22c316aae19d25ed15033794ce8b250e02c18501c1"
    },
    {
      "artifact": "FBS0B_BTC_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_BTC_USDT_2024_changes_part1.md",
      "sha256": "f2e73bb65d1da11da25fb8638d8a163cce382a65d5b37fac08bcd57f120e8e60"
    },
    {
      "artifact": "FBS0B_BTC_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_BTC_USDT_2025_changes_part1.md",
      "sha256": "b498c6043fd4f5996cc47a4fb54a9c5e31f0841b39ce49787fdb35d33a144bb8"
    },
    {
      "artifact": "FBS0B_BTC_USDT_2025_changes_part2.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_BTC_USDT_2025_changes_part2.md",
      "sha256": "2b2fb364d4e4b0b89bcdc010e1cc98914f44354398b887038f640ce5acd5ff4a"
    },
    {
      "artifact": "FBS0B_BTC_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_BTC_USDT_stop_endpoints_part1.md",
      "sha256": "6800202a72a5103afa3cfbf2a0f1e87d5a51fc7a3668c09c0044b3630b573083"
    },
    {
      "artifact": "FBS0B_PAXG_USDT_2020_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_PAXG_USDT_2020_changes_part1.md",
      "sha256": "66d64184859e6dae22ecef5467ae47cf9e1eb1c44b580629bed808a9e8f9fa34"
    },
    {
      "artifact": "FBS0B_PAXG_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_PAXG_USDT_2021_changes_part1.md",
      "sha256": "52f85c80534170c30ede54ee49911bc9ae87f32e75405aa71a544288b5caf716"
    },
    {
      "artifact": "FBS0B_PAXG_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_PAXG_USDT_2022_changes_part1.md",
      "sha256": "a3c2b5829c45ba0f705ed68bbc83fec4c699d45b5d991679ca28257486a5139d"
    },
    {
      "artifact": "FBS0B_PAXG_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_PAXG_USDT_2023_changes_part1.md",
      "sha256": "ac5b9c8d8b65af44576fb6932751524f843747d4ae5f5c6f202c100a069d1eed"
    },
    {
      "artifact": "FBS0B_PAXG_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_PAXG_USDT_2024_changes_part1.md",
      "sha256": "b735e0fb1e15bc86a0681dcb3df30063ade055b88a3196599c64893cc28151fc"
    },
    {
      "artifact": "FBS0B_PAXG_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_PAXG_USDT_2025_changes_part1.md",
      "sha256": "ba89e4372e4aa24e04301e9a3ea793fb4b77f4c91a215b2fe05115a8d4b51179"
    },
    {
      "artifact": "FBS0B_PAXG_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_PAXG_USDT_stop_endpoints_part1.md",
      "sha256": "2bbd8323e1dfb881e8a70cf77c0e9ce214b597d6a425e8c97ea98a3ce24eceb1"
    },
    {
      "artifact": "FBS0B_SPY_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_SPY_USDT_2021_changes_part1.md",
      "sha256": "b3be084d613d90bbd4568b05af04c1ed97b413a6330497dcf389d5193ee9aede"
    },
    {
      "artifact": "FBS0B_SPY_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_SPY_USDT_2022_changes_part1.md",
      "sha256": "c889a2e6511c4b145ed37ad1b0518fb3c50dcabbb6042f7249909d69179655cd"
    },
    {
      "artifact": "FBS0B_SPY_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_SPY_USDT_2023_changes_part1.md",
      "sha256": "e4cb06222bbc517c2f2825f59167498be0fbc3ee96a459ccb2b3b949c8063a92"
    },
    {
      "artifact": "FBS0B_SPY_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_SPY_USDT_2024_changes_part1.md",
      "sha256": "6c8ac444a55df461ce5b4a26ccaa000bf62ffc38492002600b378bcc2815ccc8"
    },
    {
      "artifact": "FBS0B_SPY_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_SPY_USDT_2025_changes_part1.md",
      "sha256": "248d109abd68b0f8ef9c6906aee1157c9161fa2892ac39a31cab379031e17a95"
    },
    {
      "artifact": "FBS0B_SPY_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_SPY_USDT_stop_endpoints_part1.md",
      "sha256": "d090de974b8d3d07d2af399742bb8282c4c1b9e710336b1614a127115c8795c9"
    },
    {
      "artifact": "FBS0B_divergence_summary.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0B_divergence_summary.md",
      "sha256": "50f3bc8cb1745bc6a0a78be9be4cae7cbd2e4ded15df6617ea7f1ee21d9a4d6b"
    },
    {
      "artifact": "FBS0C_BTC_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_BTC_USDT_2021_changes_part1.md",
      "sha256": "6fd2a7f2850c337ae1a0ea1223ad0c692121769b2d944a70d135004f15b9fc24"
    },
    {
      "artifact": "FBS0C_BTC_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_BTC_USDT_2022_changes_part1.md",
      "sha256": "0ad7a573baaead70085f95741709e2005ae13987aa30663c015f7bfb00f5553c"
    },
    {
      "artifact": "FBS0C_BTC_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_BTC_USDT_2023_changes_part1.md",
      "sha256": "782cd9e30884a68c1e217d700448d1799b97499e1b9763998f67e7677ef775e3"
    },
    {
      "artifact": "FBS0C_BTC_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_BTC_USDT_2024_changes_part1.md",
      "sha256": "f1a05ac5717dc9b74ee749b90d63cd32cada301874208ae3e8dc6aebbe904437"
    },
    {
      "artifact": "FBS0C_BTC_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_BTC_USDT_2025_changes_part1.md",
      "sha256": "f7d3ca0d9eb5fdec7a487bc2c3480df44ce9eac8ebad60413ced5b753aa165a5"
    },
    {
      "artifact": "FBS0C_BTC_USDT_2025_changes_part2.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_BTC_USDT_2025_changes_part2.md",
      "sha256": "1c1ab4a403a9cad99887afd707ac07b87b552a262490afeaa80569549919d7cc"
    },
    {
      "artifact": "FBS0C_BTC_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_BTC_USDT_stop_endpoints_part1.md",
      "sha256": "1e2eb1deec299bb733936e23cbd4f968386bdadacce166bde278fbef4e1a5be8"
    },
    {
      "artifact": "FBS0C_PAXG_USDT_2020_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_PAXG_USDT_2020_changes_part1.md",
      "sha256": "85e1b6f337e7a3947ddcfae64e8e22e71041aa28ec35fa564ec78da2ceef2a85"
    },
    {
      "artifact": "FBS0C_PAXG_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_PAXG_USDT_2021_changes_part1.md",
      "sha256": "b6b10cc6a061674796cc830dc2214a9e25e42ed95ea21e52e30f716ee57b5441"
    },
    {
      "artifact": "FBS0C_PAXG_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_PAXG_USDT_2022_changes_part1.md",
      "sha256": "3bc90922082389dea0702a83ec11e9de05e4809b77214d13f3dfac19f25e70a2"
    },
    {
      "artifact": "FBS0C_PAXG_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_PAXG_USDT_2023_changes_part1.md",
      "sha256": "af2e5cb8fa41c05c00e937d16a386db18a29d9acd338193981ae4807a795a1e5"
    },
    {
      "artifact": "FBS0C_PAXG_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_PAXG_USDT_2024_changes_part1.md",
      "sha256": "4724d4f8ace9e828643fab737b1ea3e474319ea91241d983905534e858ea9f6c"
    },
    {
      "artifact": "FBS0C_PAXG_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_PAXG_USDT_2025_changes_part1.md",
      "sha256": "304f3dc6fc7f339d3b1f19025dd18097a2ff87df2803a426ef4536aa24bc07ff"
    },
    {
      "artifact": "FBS0C_PAXG_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_PAXG_USDT_stop_endpoints_part1.md",
      "sha256": "f427d0b6af66e66a5b00d29ff5f14ba8af228ce9cbb574c146ca54de2be4dcfb"
    },
    {
      "artifact": "FBS0C_SPY_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_SPY_USDT_2021_changes_part1.md",
      "sha256": "382e8279be4ca8e0dfd426de06f224a36b90cdd9e4ca31ac5b0b6d9512b9e90e"
    },
    {
      "artifact": "FBS0C_SPY_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_SPY_USDT_2022_changes_part1.md",
      "sha256": "4863ee58f35ff5001ffe824f45f9ca5704d49ccabe4c6192e3daaed9a38d0837"
    },
    {
      "artifact": "FBS0C_SPY_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_SPY_USDT_2023_changes_part1.md",
      "sha256": "85a3fd8a336f198da8aa65b5bc1ce04e69a70a58558f550919ed115ddd5b5a07"
    },
    {
      "artifact": "FBS0C_SPY_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_SPY_USDT_2024_changes_part1.md",
      "sha256": "d86d91932df7aded87a8a6079439872a59ffeecb324637dd2ead53589ed7cd3d"
    },
    {
      "artifact": "FBS0C_SPY_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_SPY_USDT_2025_changes_part1.md",
      "sha256": "06a8b3ecf9aa6d9987501150994fe2866a56bb514bda2cceb79a5961db8a9d74"
    },
    {
      "artifact": "FBS0C_SPY_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_SPY_USDT_stop_endpoints_part1.md",
      "sha256": "72a7f34fc570fad23645d3e6b0e037a5aa06514dbfd026aad60dbf4266786397"
    },
    {
      "artifact": "FBS0C_divergence_summary.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS0C_divergence_summary.md",
      "sha256": "34a09fa733411e5aca31e4356dcd2e6e5242d81f4968bd03189f15daa6da925a"
    },
    {
      "artifact": "FBS1B_BTC_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_BTC_USDT_2022_changes_part1.md",
      "sha256": "7f7671bb228e9731fee1af84a472ac46b3daec9250263d03e4a834ac93692cdc"
    },
    {
      "artifact": "FBS1B_BTC_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_BTC_USDT_2023_changes_part1.md",
      "sha256": "45d7ca2ce42b1d4a3c664e7647e4bd0338ad740c60cd2d9290d43fbf38368c7f"
    },
    {
      "artifact": "FBS1B_BTC_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_BTC_USDT_2024_changes_part1.md",
      "sha256": "d9631af63f7aee3fb541127549918eee9e00049ecfa90a0d68e1a14ba890865a"
    },
    {
      "artifact": "FBS1B_BTC_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_BTC_USDT_2025_changes_part1.md",
      "sha256": "3dd9234c5f51bd1c4ae8a08bde39eeb67806895955cee373fb3913ae434cab58"
    },
    {
      "artifact": "FBS1B_BTC_USDT_2025_changes_part2.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_BTC_USDT_2025_changes_part2.md",
      "sha256": "0ce98aed1fcf19a468e0134c2a1092dc308f71b0b6b1edbf3d30272c74b93407"
    },
    {
      "artifact": "FBS1B_BTC_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_BTC_USDT_stop_endpoints_part1.md",
      "sha256": "d24d6d15bb374feb23c51e9abc3c2135ea8c6fa6284f9e2d6f20faf31b43d6bd"
    },
    {
      "artifact": "FBS1B_PAXG_USDT_2020_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_PAXG_USDT_2020_changes_part1.md",
      "sha256": "66d64184859e6dae22ecef5467ae47cf9e1eb1c44b580629bed808a9e8f9fa34"
    },
    {
      "artifact": "FBS1B_PAXG_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_PAXG_USDT_2021_changes_part1.md",
      "sha256": "21b86ed2f32a17dfd25987a5a7e36683bd4c4b4650aca4900d8a35e6cd0e134b"
    },
    {
      "artifact": "FBS1B_PAXG_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_PAXG_USDT_2022_changes_part1.md",
      "sha256": "c460d8977ebb5028097ca4ac2bcc13e45488ad3cdf0366a7f928753ffdf1cdbf"
    },
    {
      "artifact": "FBS1B_PAXG_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_PAXG_USDT_2023_changes_part1.md",
      "sha256": "9bfd4d27928a5163191c7b31e7985c2bf278b9fb1fce4fe3817713632085cb28"
    },
    {
      "artifact": "FBS1B_PAXG_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_PAXG_USDT_2024_changes_part1.md",
      "sha256": "81f29e2bf712fb2b3e59c8bff418ad8f2027dcb7c1e220bc62a3e6b19f313581"
    },
    {
      "artifact": "FBS1B_PAXG_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_PAXG_USDT_2025_changes_part1.md",
      "sha256": "4b0d4a07044250ccc5fd6ac90f81dfa3c974f2ac68c8383a0efab8d201f9b1e1"
    },
    {
      "artifact": "FBS1B_PAXG_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_PAXG_USDT_stop_endpoints_part1.md",
      "sha256": "02b6936dfc3d274a8ea042a1e3cae8e2406c10689382e80a890e35996bf97f9e"
    },
    {
      "artifact": "FBS1B_SPY_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_SPY_USDT_2021_changes_part1.md",
      "sha256": "223e84f79366d369b9e7f6e2ae56572dd09ac4735467c5ac205ca6c31007b459"
    },
    {
      "artifact": "FBS1B_SPY_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_SPY_USDT_2022_changes_part1.md",
      "sha256": "ce90f746b9e1d52362d11bdfa5f38304b5dfd534123ab265690177071508cc5a"
    },
    {
      "artifact": "FBS1B_SPY_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_SPY_USDT_2023_changes_part1.md",
      "sha256": "fddcf6d388489437913fc437905f546783cd8988092ec21f26124b47d732d27b"
    },
    {
      "artifact": "FBS1B_SPY_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_SPY_USDT_2024_changes_part1.md",
      "sha256": "7d05d68992e7f1fe8ee96eb42a94aac29ea426716ea51c218c461c08ce349124"
    },
    {
      "artifact": "FBS1B_SPY_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_SPY_USDT_2025_changes_part1.md",
      "sha256": "f584b4bd0ced1a94bae5a2ecfc572f2b0b228a8ae68703762dcc0763291ccfeb"
    },
    {
      "artifact": "FBS1B_SPY_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_SPY_USDT_stop_endpoints_part1.md",
      "sha256": "397589765786b539254b18b4d10d70719c382da15c2bb7df491158faa962c292"
    },
    {
      "artifact": "FBS1B_divergence_summary.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1B_divergence_summary.md",
      "sha256": "43a607c6c4675b2b95fe5f8cf6935787f7bafe27ae9bfef49f0b9462faa4623e"
    },
    {
      "artifact": "FBS1C_BTC_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_BTC_USDT_2022_changes_part1.md",
      "sha256": "9dec974c41dffdca1c45dc9756a93853578634506b7cdfaec2c9505d6a37bcc8"
    },
    {
      "artifact": "FBS1C_BTC_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_BTC_USDT_2023_changes_part1.md",
      "sha256": "739fcccc23356b1fe85a785f876710b918a85db0292ad85ec70eb94e7e0afafd"
    },
    {
      "artifact": "FBS1C_BTC_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_BTC_USDT_2024_changes_part1.md",
      "sha256": "3abf85fc60e2f50039a4b8e31891388e19b7f41fd2c42251eab3e8e7446ee8f9"
    },
    {
      "artifact": "FBS1C_BTC_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_BTC_USDT_2025_changes_part1.md",
      "sha256": "fe52e2701ff890208f2ba03e256a403ffe02874e783689b302313c40f557e5a3"
    },
    {
      "artifact": "FBS1C_BTC_USDT_2025_changes_part2.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_BTC_USDT_2025_changes_part2.md",
      "sha256": "f1cabecebbaefa545621860978142df28a450453ab44de7058d876b69058b4cf"
    },
    {
      "artifact": "FBS1C_BTC_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_BTC_USDT_stop_endpoints_part1.md",
      "sha256": "672034f364b0b4c07bf489196f4f4668ee708e8e351f211b21c2838dccbad94c"
    },
    {
      "artifact": "FBS1C_PAXG_USDT_2020_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_PAXG_USDT_2020_changes_part1.md",
      "sha256": "85e1b6f337e7a3947ddcfae64e8e22e71041aa28ec35fa564ec78da2ceef2a85"
    },
    {
      "artifact": "FBS1C_PAXG_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_PAXG_USDT_2021_changes_part1.md",
      "sha256": "366e2c6d75ddf8db718ec912515234c6bf995d9855034404d593e5a15d0316aa"
    },
    {
      "artifact": "FBS1C_PAXG_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_PAXG_USDT_2022_changes_part1.md",
      "sha256": "17f383f4290f737ecfe6f8f3a905cc03841332bb40397070a5f2b6f78e3f38fe"
    },
    {
      "artifact": "FBS1C_PAXG_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_PAXG_USDT_2023_changes_part1.md",
      "sha256": "02411a783b861d70591a913d12fdee20adcd33120c8663fbd850fb4804c02917"
    },
    {
      "artifact": "FBS1C_PAXG_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_PAXG_USDT_2024_changes_part1.md",
      "sha256": "7256d0435b8a5757c7eeb5d8b7a10a4ecc8536b97517e974cda43dad697a87b3"
    },
    {
      "artifact": "FBS1C_PAXG_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_PAXG_USDT_2025_changes_part1.md",
      "sha256": "93d6fb83121d08a9ca9e67f4bcd3cd1dc644d91d35c4f3c4ee9f14fbe10f1564"
    },
    {
      "artifact": "FBS1C_PAXG_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_PAXG_USDT_stop_endpoints_part1.md",
      "sha256": "2847f6a98ecfbc19187cd4b0b33b6861ad67601d284971ab7aecf45b5baf29c6"
    },
    {
      "artifact": "FBS1C_SPY_USDT_2021_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_SPY_USDT_2021_changes_part1.md",
      "sha256": "f2ed4b27cebc285eb9ff40d4bf0ca7a2a8c5865006c0612e18a89fff8f73dfc2"
    },
    {
      "artifact": "FBS1C_SPY_USDT_2022_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_SPY_USDT_2022_changes_part1.md",
      "sha256": "0ed466d5b3e55e528937163a76ce63ad9cf79d65b05d338b12f1541cfd33a693"
    },
    {
      "artifact": "FBS1C_SPY_USDT_2023_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_SPY_USDT_2023_changes_part1.md",
      "sha256": "63ae853ba20039bb679a0aa319e580a74d14df98bed249278a14e9a4b4c3dba7"
    },
    {
      "artifact": "FBS1C_SPY_USDT_2024_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_SPY_USDT_2024_changes_part1.md",
      "sha256": "6f391162041abf85f97cfc45a8b74e5b34b4044f2efe2e81418bad8291de72d8"
    },
    {
      "artifact": "FBS1C_SPY_USDT_2025_changes_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_SPY_USDT_2025_changes_part1.md",
      "sha256": "618a4a29b019e4bb7093f6d71732e402d84b76cef49def42824d9058e97ec0af"
    },
    {
      "artifact": "FBS1C_SPY_USDT_stop_endpoints_part1.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_SPY_USDT_stop_endpoints_part1.md",
      "sha256": "55f5111f6ac6a5a2b2cc50cd58e38b332c4c59e9e155afcd43cc18efecda9576"
    },
    {
      "artifact": "FBS1C_divergence_summary.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_FBS1C_divergence_summary.md",
      "sha256": "cc0256c4e70fc5da0f8a5125b1d1118da4dc3d72ba61782780336d8802eedba3"
    },
    {
      "artifact": "fixedBE_implementation_contrasts.json",
      "report": "strategies/MultiAssetRetestBtcShort4h/reports/X03_R3_FIXEDBE_DATA_fixedBE_implementation_contrasts.md",
      "sha256": "7b6b5f7761d14408397fcc9268ee98da5c6cedfa550b1a50dfb48f54c4249862"
    }
  ]
}
```
