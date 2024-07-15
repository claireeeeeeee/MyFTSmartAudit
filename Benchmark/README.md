<div align="center">
  <img src="../images/logo_FTAudit.jpg" height="80" alt="FTAudit Logo">

  # FTAudit Evaluation Dataset and Resources
</div>

## 🔗 Dataset and Resources
| Type | Description | Source | HuggingFace |
|------|-------------|--------|-------------|
| 🛠️ **Detectable Dataset** | Curated smart contracts with known vulnerabilities | [Smartbugs](https://github.com/smartbugs/smartbugs-curated) | [📥 Download](https://huggingface.co/datasets/weifar/DetectableDataset) |
| ⚙️ **Contest Dataset** | Vulnerabilities found in DeFi project audits | [Web3bugs](https://github.com/ZhangZhuoSJTU/Web3Bugs) | [📥 Download](https://huggingface.co/datasets/weifar/ContestDataset) |
| 🛜 **Large Real-world Dataset** | Actual deployed Ethereum contracts | [Etherscan](https://etherscan.io/) | [📥 Download](https://huggingface.co/datasets/weifar/LargeRealworldDataset) |


## 📊 Dataset Distribution

### 1. Detectable Dataset
<div align="center">
  <img src="https://quickchart.io/chart?c={type:'pie',data:{labels:['Randomness predictable','Reentrancy','Unchecked low-level calls','Others','Denial-of-Service','Front-running','Access control','Arithmetic','Time manipulation'],datasets:[{data:[15,31,72,4,6,5,21,22,6]}]},options:{plugins:{legend:{position:'bottom',labels:{boxWidth:12}}}}}" width="300" alt="Detectable Dataset Distribution">
</div>

|ID| Vulnerability Type                            |  Count                               |
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
|| **Total**| **182**|

### 2. Contest Dataset
<div align="center">
  <img src="https://quickchart.io/chart?c={type:'pie',data:{labels:['Detectable','Undetectable'],datasets:[{data:[128,248]}]}}" width="400" alt="Contest Dataset Distribution">
</div>

|ID| Type                            | Vulnerability Count                               |
| ------------------------------- | --------------------------------------- | --------------------------------------- |
|1|Detectable| 128|
|2|Undetectable| 248|
| | **Total** | **376** |

### 3. Contest Dataset

This dataset incorporates actual contracts deployed on the Ethereum blockchain, ensuring that our evaluations reflect real-world usage patterns and providing a realistic and in-depth assessment of the model's performance.

- **Total Contracts**: 11,510
- **Date Range**: From 2017-07-08 08:26:34 UTC to 2022-05-05 23:59:47 UTC
- **Source**: [Etherscan](https://etherscan.io/)