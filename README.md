# Iyuno Agent Portfolio

채용공고의 요구사항을 실제로 구현해 보는 AI Agent 포트폴리오 프로젝트입니다.

본 프로젝트는 **Iyuno AI Agent Engineer 채용공고**를 참고하여 설계했습니다.

## 1. 프로젝트 소개

공개된 보안·기술 문서를 수집하고, 사용자의 질문에 관련된 정보를 검색하여 근거와 함께 답변하는 **AI Agent 시스템**을 구현하는 것을 목표로 합니다.

단순한 ChatGPT 질문·답변이 아니라 다음과 같은 기능을 단계적으로 구현합니다.

* 문서 수집 및 전처리
* 문서 Chunking
* Embedding
* Vector Search
* RAG 기반 검색 및 답변
* 답변에 출처(Citation) 표시
* Tool Calling
* 계산기 및 외부 API 활용
* 질문 데이터셋을 이용한 정량 평가
* 오류 분석 및 성능 개선

## 2. 프로젝트 목표

이 프로젝트를 통해 AI Agent Engineer 채용공고에서 요구하는 다음 역량을 실제 결과물로 보여주는 것을 목표로 합니다.

| 채용공고 요구사항                 | 프로젝트 구현 목표                   |
| ------------------------- | ---------------------------- |
| LLM 기반 AI Agent 시스템 설계·개발 | AI Agent 구조 설계 및 구현          |
| RAG 검색·응답 시스템             | 문서 검색 기반 RAG 구현              |
| Tool Calling              | 외부 도구 및 API 호출               |
| API·데이터베이스 통합             | 프로젝트에 필요한 API/데이터 연동         |
| 다단계 Workflow              | 질문에 따라 검색과 도구를 선택하는 Workflow |
| 평가 및 개선                   | 평가 데이터셋과 성능 지표를 통한 분석        |
| Feedback Loop             | 사용자 수정/피드백을 저장하고 개선에 활용      |

## 3. 프로젝트 아키텍처

현재 목표 아키텍처는 다음과 같습니다.

사용자 질문
↓
Agent / Router
↓
RAG Retriever 또는 Tools / APIs
↓
검색 결과 및 도구 실행 결과
↓
답변 + 출처(Citation)
↓
평가 및 Feedback

## 4. 주요 기술

프로젝트 구현 과정에서 다음 기술을 활용할 예정입니다.

* Python
* LLM
* RAG
* Embedding
* Vector Search
* Tool Calling
* API
* FastAPI 또는 Streamlit
* pytest
* GitHub Actions

## 5. 평가 계획

프로젝트가 완성된 후 30개 이상의 질문을 이용하여 성능을 평가할 예정입니다.

평가 항목:

* Recall@k
* Faithfulness
* Latency
* Token Cost
* 오류 및 실패 사례

평가 결과는 `evaluation/metrics.json`과 그래프로 정리할 예정입니다.

## 6. 데이터 및 출처

프로젝트에는 공개적으로 이용 가능한 보안·기술 문서를 사용합니다.

각 데이터에 대해 다음 정보를 기록할 예정입니다.

* 문서명
* 원본 URL
* 출처
* 라이선스
* 수집/생성일

## 7. 현재 진행 상황

* [x] GitHub Repository 생성
* [x] README 초안 작성
* [ ] 공개 문서 수집
* [ ] 문서 Chunking
* [ ] Embedding 및 Vector Search
* [ ] RAG 구현
* [ ] Citation 구현
* [ ] Tool Calling 구현
* [ ] 평가 데이터셋 30개 이상 구축
* [ ] Evaluation 및 Metrics 작성
* [ ] pytest 및 CI 구성
* [ ] Streamlit/FastAPI 데모
* [ ] 데모 영상 제작

## 8. 프로젝트의 한계

본 프로젝트는 학습 및 포트폴리오 목적으로 제작됩니다.

실제 기업의 내부 데이터나 비공개 자료를 사용하지 않으며, 공개된 자료를 기반으로 AI Agent의 구조와 기능을 구현합니다.

또한 프로젝트의 평가 결과는 제한된 평가 데이터셋을 기반으로 하므로 실제 서비스 환경의 성능을 그대로 의미하지 않습니다.

## 9. 참고 채용공고

**Iyuno AI Agent Engineer**

* Location: Seoul
* Work Type: Hybrid / Full-time
* Requisition: JR101122

채용공고:
https://iyuno.wd3.myworkdayjobs.com/careers/job/seoul/ai-agent-engineer_jr101122

## 10. 프로젝트 목적

이 저장소는 채용공고의 요구사항을 단순히 나열하는 것이 아니라,

**채용공고 → 요구 역량 분석 → 실제 구현 → 평가 → 결과 문서화**
