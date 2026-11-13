# Dr. A.S. Oni (MB;BS Ibadan)

### Clinical medicine meets machine learning

I'm a medical doctor in Ibadan, Nigeria, building machine learning systems for healthcare, with a focus on medical imaging, clinical language models and retrieval-augmented generation. My clinical training shapes how I frame problems, choose metrics and judge whether a model is actually useful at the bedside.

---

## Research

**Parameter-efficient adaptation of radiology foundation models for TB detection**
A systematic comparison of LoRA, BitFit, linear probing and full fine-tuning on BiomedCLIP and RAD-DINO, trained on Shenzhen chest X-rays and tested on three external datasets (Montgomery, TBX11K, Kaggle TB). 13 configurations × 5 folds, 65 training runs and 195 external evaluations.
Preprint: [doi:10.5281/zenodo.21480007](https://doi.org/10.5281/zenodo.21480007)

---

## Projects

### [Ask My Docs](https://github.com/AyotundeOni/ask-my-docs): production-style RAG chatbot
Hybrid search (vector + BM25) with cross-encoder reranking, citation-grounded answers, input/output guardrails and a RAGAS evaluation pipeline. FastAPI backend, Streamlit UI, swappable Groq/Ollama LLM backend.
`Python` `FastAPI` `ChromaDB` `RAG` `RAGAS`

### [Patho-Bot](https://github.com/AyotundeOni/Kaggle-Capstone): low-resource malaria pathology agent
Kaggle capstone. A fine-tuned YOLO11 nano detector counts parasites in blood smears, and a Gemini-based agent turns the counts into WHO-guideline-grounded treatment advice.
`Python` `YOLO` `Google ADK` `Gemini`

### [Shopify Concierge](https://github.com/AyotundeOni/Customer-Support-Chatbot-RAG-Fine-tuned-LLM-): agentic customer-support assistant
Mistral 12B fine-tuned with Unsloth on about 1,500 Q&A pairs, combined with Pinecone RAG, sentiment analysis and automatic ticket escalation.
`Python` `LangChain` `Pinecone` `Streamlit`

### [Clinical NER Annotation & QA Toolkit](https://github.com/AyotundeOni/clinical-ner-annotation-toolkit)
Parsing, boundary checks, CoNLL/IOB2 and spaCy conversion, and cross-corpus label-consistency QA on the NCBI Disease Corpus. Built on expert gold labels; see the attribution file for credit.

### [Malaria Cell Annotation & QA Toolkit](https://github.com/AyotundeOni/malaria-annotation-toolkit)
Bounding-box QA (12 automated checks), COCO/YOLO conversion and edge-case escalation for the BBBC041 *P. vivax* blood-smear dataset.

---

## Toolbox

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
</p>

---

## Where I'm headed

A research-focused path in medical imaging AI and health informatics: graduate research where clinical context and machine learning meet, with the long-term aim of building ethical, effective tools that reduce health disparities.

## Contact

- LinkedIn: [ayotundeoni](https://www.linkedin.com/in/ayotundeoni)
- Email: [ayotunde326@gmail.com](mailto:ayotunde326@gmail.com)
