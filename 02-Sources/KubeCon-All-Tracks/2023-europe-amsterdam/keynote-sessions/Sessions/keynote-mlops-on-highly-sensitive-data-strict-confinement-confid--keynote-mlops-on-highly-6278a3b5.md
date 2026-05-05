---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Keynote Sessions"
themes: ["AI ML", "Storage Data"]
speakers: ["Maciej Mazur", "Principal AI/ML Engineer", "Canonical", "Andreea Munteanu", "AI/ML Product Manager", "Canonical"]
sched_url: https://kccnceu2023.sched.com/event/1HyQX/keynote-mlops-on-highly-sensitive-data-strict-confinement-confidential-computing-and-tokenization-protecting-privacy-maciej-mazur-principal-aiml-engineer-canonical-andreea-munteanu-aiml-product-manager-canonical
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+MLOps+on+Highly+Sensitive+Data+-+Strict+Confinement%2C+Confidential+Computing%2C+and+Tokenization+Protecting+Privacy+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Keynote: MLOps on Highly Sensitive Data - Strict Confinement, Confidential Computing, and Tokenization Protecting Privacy - Maciej Mazur, Principal AI/ML Engineer, Canonical & Andreea Munteanu, AI/ML Product Manager, Canonical

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Maciej Mazur, Principal AI/ML Engineer, Canonical, Andreea Munteanu, AI/ML Product Manager, Canonical
- Schedule: https://kccnceu2023.sched.com/event/1HyQX/keynote-mlops-on-highly-sensitive-data-strict-confinement-confidential-computing-and-tokenization-protecting-privacy-maciej-mazur-principal-aiml-engineer-canonical-andreea-munteanu-aiml-product-manager-canonical
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+MLOps+on+Highly+Sensitive+Data+-+Strict+Confinement%2C+Confidential+Computing%2C+and+Tokenization+Protecting+Privacy+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Keynote: MLOps on Highly Sensitive Data - Strict Confinement, Confidential Computing, and Tokenization Protecting Privacy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyQX/keynote-mlops-on-highly-sensitive-data-strict-confinement-confidential-computing-and-tokenization-protecting-privacy-maciej-mazur-principal-aiml-engineer-canonical-andreea-munteanu-aiml-product-manager-canonical
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+MLOps+on+Highly+Sensitive+Data+-+Strict+Confinement%2C+Confidential+Computing%2C+and+Tokenization+Protecting+Privacy+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iYy3EdgjnhE
- YouTube title: Keynote: MLOps on Highly Sensitive Data - Strict Confinement, Con... Maciej Mazur & Andreea Munteanu
- Match score: 0.795
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/keynote-mlops-on-highly-sensitive-data-strict-confinement-confidential/iYy3EdgjnhE.txt
- Transcript chars: 12037
- Keywords: actually, process, public, confidential, tokenization, source, kubeflow, machine, learning, whenever, computing, science, michelle, secure, inference, strict, privacy, andrea

### Resumo baseado na transcript

um next up our presenters are mashia major and Andre montaneo so martial is a principal AI engineer economical and Andrea is a AIML product manager at canonical and today they will bring us through a case study of a life science company that creates customized treatments based on DNA using Cloud native Technologies like kubernetes and kubeflow so please welcome mache and Andrea [Applause] [Music] thank you hello glad to be here today I'll talk about superheroes reminiscents of our childhood dreams of being Superman or Batman I'll take

### Excerpt da transcript

um next up our presenters are mashia major and Andre montaneo so martial is a principal AI engineer economical and Andrea is a AIML product manager at canonical and today they will bring us through a case study of a life science company that creates customized treatments based on DNA using Cloud native Technologies like kubernetes and kubeflow so please welcome mache and Andrea [Applause] [Music] thank you hello glad to be here today I'll talk about superheroes reminiscents of our childhood dreams of being Superman or Batman I'll take the chance and be a hero saving people's lives forget about Andrea for now I'm Michelle a life science researcher working on some of the most Innovative projects Dynamic Stephen drug discovery is a very new and promising solution as drag targets with human support are more likely to be successful it is a new approach in the industry that uses genome data to develop targeted treatments for different diseases with the rise of generative AI if you think of charge GPT for example I thought I could make use of artificial intelligence however I deeply care about my patients data so there is one question that I had in mind Patrick is it safe to use highly sensitive data for machine learning initiatives yeah so we are doing a lot to make it secure and today I'll be myself a Solutions architect because I don't really have acting capabilities so any project using machine learning is a software project so obviously all the devsecops principles apply we are still doing CV patching and that kind of security however what is important for us as ml Engineers to remember about additional things that we need to take care of first of all the inputs to the whole process so any kind of data that we use to train the model and also any data that we use to actually ping the inference and points needs to be checked so we are doing a lot on monitoring for data drift or model or drift and make sure that that is safe another area that me and my colleagues are focusing on is explainable AI so obviously we don't want the model to be a complete Black Box where we don't actually understand why certain decision is made we want to be able to zoom in to any decision point and make sure that it was taken in the right way and what we'll be talking about today the third area is the envelopes so with envelopes machine learning operations we are looking into setting up processes from drawing blood samples in the sampling station itself to getting the data into the
