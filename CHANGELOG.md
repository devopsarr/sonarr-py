# Changelog

## [1.1.1](https://github.com/devopsarr/sonarr-py/compare/v1.1.0...v1.1.1) (2025-09-02)


### Bug Fixes

* **deps:** update dependency sonarr/sonarr to v4.0.13.2932 ([88879d2](https://github.com/devopsarr/sonarr-py/commit/88879d28b1960198e2c83aa7a6da9c6ca65b2d84))
* **deps:** update dependency sonarr/sonarr to v4.0.15.2941 ([001b87a](https://github.com/devopsarr/sonarr-py/commit/001b87a040042151542d0a3f2724c2c03014dac2))
* **deps:** update openapitools/openapi-generator-cli docker tag to v7.12.0 ([9ffdd19](https://github.com/devopsarr/sonarr-py/commit/9ffdd196783e1a88a855dbe17b1280571c15bc5f))
* **deps:** update openapitools/openapi-generator-cli docker tag to v7.15.0 ([afb4ac8](https://github.com/devopsarr/sonarr-py/commit/afb4ac87fcd221e3ee11b17e32eec12aad83afaf))

## [1.1.0](https://github.com/devopsarr/sonarr-py/compare/v1.0.2...v1.1.0) (2025-01-20)


### Features

* remove broken root api path ([7f7aa0f](https://github.com/devopsarr/sonarr-py/commit/7f7aa0fdee97be86fadf0f9100d9831bd6866edc))


### Bug Fixes

* **deps:** update dependency sonarr/sonarr to v4.0.11.2680 ([70a29ba](https://github.com/devopsarr/sonarr-py/commit/70a29baf226724beadbf4171306d636be9ddc296))
* **deps:** update dependency sonarr/sonarr to v4.0.12.2823 ([93ff710](https://github.com/devopsarr/sonarr-py/commit/93ff7104a684c8e2c26bb0b23865d44bc5db9dc2))
* **deps:** update openapitools/openapi-generator-cli docker tag to v7.10.0 ([b5dd6f8](https://github.com/devopsarr/sonarr-py/commit/b5dd6f8af0e5c8ce26c2914900703c1cf8f93075))
* **deps:** update openapitools/openapi-generator-cli docker tag to v7.11.0 ([8a1e7ad](https://github.com/devopsarr/sonarr-py/commit/8a1e7ad0ad3df7361e7ee1767fe0d1beeea55710))

## [1.0.2](https://github.com/devopsarr/sonarr-py/compare/v1.0.1...v1.0.2) (2024-10-08)


### Bug Fixes

* **deps:** update openapitools/openapi-generator-cli docker tag to v7.9.0 ([0d61f0e](https://github.com/devopsarr/sonarr-py/commit/0d61f0eedb41c66e5bd925ef50877f345f3271a3))

## [1.0.1](https://github.com/devopsarr/sonarr-py/compare/v1.0.0...v1.0.1) (2024-02-21)


### Bug Fixes

* map Field to ContractField to avoid pydantic issue ([73829ad](https://github.com/devopsarr/sonarr-py/commit/73829adcd102d9fdbb6fd10c719da33ee28cdfdb))

## [1.0.0](https://github.com/devopsarr/sonarr-py/compare/v1.0.0...v1.0.0) (2024-02-20)


### ⚠ BREAKING CHANGES

* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x

### Features

* add autotagging ([2164d37](https://github.com/devopsarr/sonarr-py/commit/2164d3798cbc25841b2272645caf20df881d8bcb))
* add sonarr auto tagging schema return type ([feeea7c](https://github.com/devopsarr/sonarr-py/commit/feeea7c43dcef2f2a0b3216b67de2d22dfed8f44))
* **devopsarr/prowlarr-py#11:** add request timeout to config ([ff03ca7](https://github.com/devopsarr/sonarr-py/commit/ff03ca7014593f5d53a2346c16106602e3213aa6))
* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x ([8884625](https://github.com/devopsarr/sonarr-py/commit/8884625e16f41709364cc1a181b13eaaba82db01))
* initial config ([23fca6d](https://github.com/devopsarr/sonarr-py/commit/23fca6d0fa7938969d8cf29c4eea644d78feee1b))
* inject api version into readme ([231b4e4](https://github.com/devopsarr/sonarr-py/commit/231b4e4febec0565cdc2290a7afe4d303ceed07a))
* move to code generator ([ab19560](https://github.com/devopsarr/sonarr-py/commit/ab195605852b04816dc03d5b7b1564abb9e1613f))
* pin openapi version and add version management ([0ea6441](https://github.com/devopsarr/sonarr-py/commit/0ea6441677bfcf51b0393fa61bb7dd173e9129f4))
* sdk generation alignment ([456dd81](https://github.com/devopsarr/sonarr-py/commit/456dd81ec9935886201efa9ca876b31db6fc5cc5))
* series lookup get to list ([b7c863e](https://github.com/devopsarr/sonarr-py/commit/b7c863e80d66e407fb98ad1557b7c97108618f28))
* **sonarr:** add response type to custom format ([99990e8](https://github.com/devopsarr/sonarr-py/commit/99990e8b215d1e03d3d715ce5fa1a001a586791b))
* update composite names ([b6c3fb0](https://github.com/devopsarr/sonarr-py/commit/b6c3fb0a81a51b9e42b6e2972f0e6049a225c097))


### Bug Fixes

* **#5:** httpuri to string ([4042f23](https://github.com/devopsarr/sonarr-py/commit/4042f237b3532aea2f75cdc1d7e3be4215d3f7b5))
* **#6:** use repr of query parameters ([9ebb6af](https://github.com/devopsarr/sonarr-py/commit/9ebb6afaae82678681e92f4ec89920ca0a561b8c))
* dependency typo ([2f9a95b](https://github.com/devopsarr/sonarr-py/commit/2f9a95ba8308aadbe3152be5038ee6a0ad06a94f))
* **devopsarr/radarr-py#6:** indentation error on config ([32b69f6](https://github.com/devopsarr/sonarr-py/commit/32b69f6819c24b19d1ff6c26fa6ab539676f9a6b))
* **devopsarr/sonarr-py#6:** remove timespan validator ([b961b16](https://github.com/devopsarr/sonarr-py/commit/b961b164f5dd5bda958db6b0102d439c09bb1dea))
* import validator for components with pattern ([e168f25](https://github.com/devopsarr/sonarr-py/commit/e168f2569b27c8c2bf333e931d9b4468d6aabcc3))
* **python:** wrong release versioning on configuration.py ([6b70b2c](https://github.com/devopsarr/sonarr-py/commit/6b70b2ccc69b14896ade9522166d49c75fc3bf01))
* release please commented lines ([550cb93](https://github.com/devopsarr/sonarr-py/commit/550cb93525935553f0627ae5e69dfaf229f191da))
* remove language profile id ([592a6b3](https://github.com/devopsarr/sonarr-py/commit/592a6b397967df120882ec83dd3317e5efeff0d5))
* remove middle elements from method name ([b235b41](https://github.com/devopsarr/sonarr-py/commit/b235b4140846448fea51cf17313f68153a276752))
* set pydantic version ([6a01f14](https://github.com/devopsarr/sonarr-py/commit/6a01f14a8a7db2d196395291dae6f9bdc605a626))
* sonarr release profile required and ignored list ([1933ddc](https://github.com/devopsarr/sonarr-py/commit/1933ddc8f727f8f35f643fd4886a7f034fcd6273))
* timespan to string ([2091423](https://github.com/devopsarr/sonarr-py/commit/20914237b8aaf2e971772e26edecf8c20893db9a))


### Miscellaneous Chores

* **#41:** release 0.10.0 ([18d494e](https://github.com/devopsarr/sonarr-py/commit/18d494ef2e8a8fb5108c83765943cab663c0ef70))
* release 0.4.0 ([308e0b8](https://github.com/devopsarr/sonarr-py/commit/308e0b81a95186d76bc7d540afdee201fc21a1bb))
* release 1.0.0 ([5b2d50e](https://github.com/devopsarr/sonarr-py/commit/5b2d50e16ff901b44dba60cbdf1da3f3792eaf6c))

## [1.0.0](https://github.com/devopsarr/sonarr-py/compare/v0.10.0...v1.0.0) (2024-02-15)


### ⚠ BREAKING CHANGES

* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x

### Features

* **devopsarr/prowlarr-py#39:** update sdk generator to use pydantic 2.x ([8884625](https://github.com/devopsarr/sonarr-py/commit/8884625e16f41709364cc1a181b13eaaba82db01))
* inject api version into readme ([231b4e4](https://github.com/devopsarr/sonarr-py/commit/231b4e4febec0565cdc2290a7afe4d303ceed07a))


### Bug Fixes

* **python:** wrong release versioning on configuration.py ([6b70b2c](https://github.com/devopsarr/sonarr-py/commit/6b70b2ccc69b14896ade9522166d49c75fc3bf01))
* release please commented lines ([550cb93](https://github.com/devopsarr/sonarr-py/commit/550cb93525935553f0627ae5e69dfaf229f191da))
* remove middle elements from method name ([b235b41](https://github.com/devopsarr/sonarr-py/commit/b235b4140846448fea51cf17313f68153a276752))

## [0.10.0](https://github.com/devopsarr/sonarr-py/compare/v0.9.0...v0.10.0) (2023-10-11)


### Miscellaneous Chores

* **#41:** release 0.10.0 ([18d494e](https://github.com/devopsarr/sonarr-py/commit/18d494ef2e8a8fb5108c83765943cab663c0ef70))

## [0.9.0](https://github.com/devopsarr/sonarr-py/compare/v0.8.0...v0.9.0) (2023-08-23)


### Features

* add sonarr auto tagging schema return type ([feeea7c](https://github.com/devopsarr/sonarr-py/commit/feeea7c43dcef2f2a0b3216b67de2d22dfed8f44))

## [0.8.0](https://github.com/devopsarr/sonarr-py/compare/v0.7.0...v0.8.0) (2023-07-21)


### Features

* **sonarr:** add response type to custom format ([99990e8](https://github.com/devopsarr/sonarr-py/commit/99990e8b215d1e03d3d715ce5fa1a001a586791b))


### Bug Fixes

* set pydantic version ([6a01f14](https://github.com/devopsarr/sonarr-py/commit/6a01f14a8a7db2d196395291dae6f9bdc605a626))
* sonarr release profile required and ignored list ([1933ddc](https://github.com/devopsarr/sonarr-py/commit/1933ddc8f727f8f35f643fd4886a7f034fcd6273))

## [0.7.0](https://github.com/devopsarr/sonarr-py/compare/v0.6.2...v0.7.0) (2023-05-17)


### Features

* **devopsarr/prowlarr-py#11:** add request timeout to config ([ff03ca7](https://github.com/devopsarr/sonarr-py/commit/ff03ca7014593f5d53a2346c16106602e3213aa6))
* pin openapi version and add version management ([0ea6441](https://github.com/devopsarr/sonarr-py/commit/0ea6441677bfcf51b0393fa61bb7dd173e9129f4))

## [0.6.2](https://github.com/devopsarr/sonarr-py/compare/v0.6.1...v0.6.2) (2023-03-27)


### Bug Fixes

* **devopsarr/sonarr-py#6:** remove timespan validator ([b961b16](https://github.com/devopsarr/sonarr-py/commit/b961b164f5dd5bda958db6b0102d439c09bb1dea))

## [0.6.1](https://github.com/devopsarr/sonarr-py/compare/v0.6.0...v0.6.1) (2023-03-24)


### Bug Fixes

* **devopsarr/radarr-py#6:** indentation error on config ([32b69f6](https://github.com/devopsarr/sonarr-py/commit/32b69f6819c24b19d1ff6c26fa6ab539676f9a6b))

## [0.6.0](https://github.com/devopsarr/sonarr-py/compare/v0.5.0...v0.6.0) (2023-03-24)


### Features

* sdk generation alignment ([456dd81](https://github.com/devopsarr/sonarr-py/commit/456dd81ec9935886201efa9ca876b31db6fc5cc5))
* series lookup get to list ([b7c863e](https://github.com/devopsarr/sonarr-py/commit/b7c863e80d66e407fb98ad1557b7c97108618f28))


### Bug Fixes

* **#5:** httpuri to string ([4042f23](https://github.com/devopsarr/sonarr-py/commit/4042f237b3532aea2f75cdc1d7e3be4215d3f7b5))
* **#6:** use repr of query parameters ([9ebb6af](https://github.com/devopsarr/sonarr-py/commit/9ebb6afaae82678681e92f4ec89920ca0a561b8c))
* import validator for components with pattern ([e168f25](https://github.com/devopsarr/sonarr-py/commit/e168f2569b27c8c2bf333e931d9b4468d6aabcc3))
* timespan to string ([2091423](https://github.com/devopsarr/sonarr-py/commit/20914237b8aaf2e971772e26edecf8c20893db9a))

## [0.5.0](https://github.com/devopsarr/sonarr-py/compare/v0.4.0...v0.5.0) (2023-02-21)


### Features

* add autotagging ([2164d37](https://github.com/devopsarr/sonarr-py/commit/2164d3798cbc25841b2272645caf20df881d8bcb))

## 0.4.0 (2023-01-24)


### Features

* initial config ([23fca6d](https://github.com/devopsarr/sonarr-py/commit/23fca6d0fa7938969d8cf29c4eea644d78feee1b))
* move to code generator ([ab19560](https://github.com/devopsarr/sonarr-py/commit/ab195605852b04816dc03d5b7b1564abb9e1613f))
* update composite names ([b6c3fb0](https://github.com/devopsarr/sonarr-py/commit/b6c3fb0a81a51b9e42b6e2972f0e6049a225c097))


### Bug Fixes

* dependency typo ([2f9a95b](https://github.com/devopsarr/sonarr-py/commit/2f9a95ba8308aadbe3152be5038ee6a0ad06a94f))
* remove language profile id ([592a6b3](https://github.com/devopsarr/sonarr-py/commit/592a6b397967df120882ec83dd3317e5efeff0d5))


### Miscellaneous Chores

* release 0.4.0 ([308e0b8](https://github.com/devopsarr/sonarr-py/commit/308e0b81a95186d76bc7d540afdee201fc21a1bb))
