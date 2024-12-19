<center><img src="https://imgtr.ee/images/2024/07/03/9eea693c3d3aee90f0ea2041012aa6a1.png" alt="9eea693c3d3aee90f0ea2041012aa6a1.png" border="0" /></center>

# HiBlu: LLM Chatbot for Blu (BCA Digital)

---

## Background

Di era digital yang kompetitif saat ini, kepuasan user merupakan hal yang sangat penting khususnya dalam sektor layanan perbankan. Tanggapan yang cepat dan akurat terhadap pertanyaan user sangatlah penting untuk mempertahankan nasabah mereka. Teknologi Generative AI, khususnya Large Language Models (LLM), telah merevolusi interaksi terhadap user melalui chatbot yang cerdas dan mampu untuk menyediakan informasi dengan cepat dan tepat, serta dapat meningkatkan efisiensi *operational cost*.

---

## Introduction

HiBlu merupakan model chatbot LLM yang dibuat khusus untuk **blu** (sebuah layanan perbankan digital oleh BCA). HiBlu dirancang untuk memberikan tanggapan yang cepat dan akurat terhadap pertanyaan nasabah/calon nasabah terkait layanan **blu** guna meningkatkan waktu respon, efisiensi, dan pengalaman user.

Model chatbot LLM ini merupakan *prototype pertama* yang harapannya dapat diimplementasikan terhadap kesuluruhan layanan instansi BCA di masa depan. Dalam dokumentasi prototype ini nantinya akan dilakukan juga perbandingan hasil pemodelan antara model LLM RAG dan LLM fine-tuned.

---

## Team Members

   - [Dito Wicaksana Prasetya](https://github.com/ditoowp) as a Data Engineer.
   - [Ahmad Naufal Budianto](https://naufalbudianto.framer.website/) as a Data Analyst + Visual Designer.
   - [Gieorgie Kharismatik Kosasih](https://github.com/GieorgieK) as a Data Scientist.
   - [Darly Guntur Darris Purba](https://github.com/DarlyP) as a Data Scientist.

---

## Data Source

Data referensi jawaban pertanyaan yang sering diajukan adalah berdasarkan hasil scrapping pada laman [FAQ Blu](https://blubybcadigital.id/info/faq).

---

## RAG LLM Workflow

<center><img src="https://imgtr.ee/images/2024/07/04/8a526fd5b3fbff55170ff8138ad658d9.png" alt="8a526fd5b3fbff55170ff8138ad658d9.png" border="0" /></center>

---

## Fine Tuning LLM Workflow

<center><img src="https://imgtr.ee/images/2024/07/04/cd68f1b08bdac93e13e63ea234af44e0.png" alt="cd68f1b08bdac93e13e63ea234af44e0.png" border="0" /></center>

---

## RAFT LLM Workflow

<center><img src="https://imgtr.ee/images/2024/07/04/b4d1f6353981668b1938edc7dbf3dff1.png" alt="b4d1f6353981668b1938edc7dbf3dff1.png" border="0" /></center>

---

## File Explanation

| File | Explanation |
| --- | --- |
| `scraping.ipynb` | FAQ Web Scrapping Documentation |
| `hiblu_DAG.py` | DAG Documentation |
| `eda.ipynb` | EDA Documentation |
| `FAQ_GX.ipynb` | Great Expectation Validation Documentation |
| `rag_maverick_vecdb.ipynb` | Vector To MongoDB Documentation |
| `rag_maverick_query.ipynb` | RAG Model Documentation |
| `fine_tuning_maverick_query.ipynb` | Fine Tuning Model Documentation |
| `ragft_maverick_query.ipynb` | RAFT Model Documentation |
| `rag.py` | RAG Deployment Documentation |
| `finetuning.py` | Fine Tuning Documentation |
| `ragft.py` | RAFT Documentation |

---

## Link

* [Recording Video](https://drive.google.com/file/d/1AUtG-WBEMWUht799C6bXHG-T645zUv1c/view?usp=sharing)
* [Sample of Model Comparison](https://docs.google.com/spreadsheets/d/1C6bjPlXn09hHPvgiO1LU5f2JuIc1eKDk/edit?usp=sharing&ouid=108097674241546601906&rtpof=true&sd=true)
* [Presentation Deck](https://drive.google.com/file/d/1f4l9zLxRy-XMTeoh-R_E-1vX2rvMJmST/view?usp=sharing)