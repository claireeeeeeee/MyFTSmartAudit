<div align="center">

  <a><picture>
    <img src="../images/logo_FTAudit.jpg" height=80>
      </picture></a>
</div>

## 🔗 Dataset and Resources
| Type                            | Links                               | HuggingFace Source|
| ------------------------------- | --------------------------------------- | --------------------------------------- |
| 🛠️ **Detectable Dataset**              | [Smartbugs](https://github.com/smartbugs/smartbugs-curated) | [Download](https://huggingface.co/datasets/weifar/DetectableDataset) |
| ⚙️ **Contest Dataset**                   | [Web3bugs](https://github.com/ZhangZhuoSJTU/Web3Bugs)| [Download](https://huggingface.co/datasets/weifar/ContestDataset)|
| 🛜 **Large Real-world Dataset**            | [Etherscan](https://etherscan.io/)| [Download](https://huggingface.co/datasets/weifar/LargeRealworldDataset)|


## 🔗 Dataset Distribution

### 1. Detectable Dataset
|ID| Type                            | Vulnerability Count                               |
| ------------------------------- | --------------------------------------- | --------------------------------------- |
|V1| Randomness predictable| 15|
|V2| Reentrancy| 31|
|V3| unchecked_low_level_calls| 72|
|V4| Others| 4|
|V5| Denial-of-Service| 6|
|V6| Front-running| 5|
|V7| Access control| 21|
|V8| Arithmetic| 22|
|V9| Time manipulation| 6|
|| Total| 182|

### 2. Contest Dataset
|ID| Type                            | Vulnerability Count                               |
| ------------------------------- | --------------------------------------- | --------------------------------------- |
|1|Detectable| 128|
|2|Undetectable| 248|

### 3. Contest Dataset
This dataset incorporates actual contracts deployed on the Ethereum blockchain, ensuring that our evaluations reflect real-world usage patterns and providing a realistic and in-depth assessment of the model's performance. We collected 11,510 contracts from Etherscan, spanning from 2017-07-08 08:26:34 UTC to 2022-05-05 23:59:47 UTC.
