<div style="text-align: center;">
    <img src="https://i.postimg.cc/SKdt9NKD/HiBlu.png" alt="HiBlu.jpeg">
</div>

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

<div style="text-align: center;">
    <img src="https://i.postimg.cc/pVmRP30g/RAG-LLM.png" alt="RAG LLM Workflow">
</div>

---

## Fine Tuning LLM Workflow

<div style="text-align: center;">
    <img src="https://i.postimg.cc/4xQT8Gdh/Fine-Tune-LLM.png" alt="Fine Tuning LLM Workflow">
</div>

---

## RAFT LLM Workflow

<div style="text-align: center;">
    <img src="https://i.postimg.cc/4xQT8Gdh/Fine-Tune-LLM.png" alt="RAFT LLM Workflow">
</div>


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
