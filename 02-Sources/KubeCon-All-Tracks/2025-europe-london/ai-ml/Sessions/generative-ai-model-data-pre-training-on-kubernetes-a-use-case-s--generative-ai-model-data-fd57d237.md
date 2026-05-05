---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Storage Data", "Kubernetes Core"]
speakers: ["Alexey Roytman", "IBM", "Anish Asthana", "Red Hat"]
sched_url: https://kccnceu2025.sched.com/event/1tx6w/generative-ai-model-data-pre-training-on-kubernetes-a-use-case-study-alexey-roytman-ibm-anish-asthana-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Generative+AI+Model+Data+Pre-Training+on+Kubernetes%3A+A+Use+Case+Study+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Generative AI Model Data Pre-Training on Kubernetes: A Use Case Study - Alexey Roytman, IBM & Anish Asthana, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Alexey Roytman, IBM, Anish Asthana, Red Hat
- Schedule: https://kccnceu2025.sched.com/event/1tx6w/generative-ai-model-data-pre-training-on-kubernetes-a-use-case-study-alexey-roytman-ibm-anish-asthana-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Generative+AI+Model+Data+Pre-Training+on+Kubernetes%3A+A+Use+Case+Study+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Generative AI Model Data Pre-Training on Kubernetes: A Use Case Study.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx6w/generative-ai-model-data-pre-training-on-kubernetes-a-use-case-study-alexey-roytman-ibm-anish-asthana-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Generative+AI+Model+Data+Pre-Training+on+Kubernetes%3A+A+Use+Case+Study+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CzdX5qDgQ2U
- YouTube title: Generative AI Model Data Pre-Training on Kubernetes: A Use Case St... Alexey Roytman & Anish Asthana
- Match score: 0.895
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/generative-ai-model-data-pre-training-on-kubernetes-a-use-case-study/CzdX5qDgQ2U.txt
- Transcript chars: 19386
- Keywords: pipelines, pipeline, cubeflow, language, cluster, running, components, cubray, started, execute, simple, processing, operator, actually, create, nested, document, workflows

### Resumo baseado na transcript

Um I've been working in the cloud native AI space for the last seven years or so now. After that uh cloud infrastructure, cloud solutions and currently my focus on data processing automation. Another type of parallelism can be applied based on natural language because after uh and we're going to demonstrate it in demo after language separation uh all next steps can be run independently and execute uh for each language. These stages may or may not be linked to each other and they can operate on data the very wide variety of scales right it could be at the megabyte gigabyte level just for like local development and testing or at actual terabyte scale for when you have you know lots of data and you're doing actual data transformations. One of the issues that we were running into was how do we make it easy for our developers to like do quick local like development cycles on their laptops and then scale up to the cloud, right? So, Cubray is an operator that brings core Ray concepts such as Ray clusters, Ray jobs, and Ray serve to Kubernetes.

### Excerpt da transcript

Hi everyone, my name is Anish Astana. I'm an engineering manager with the open shift AI group at Red Hat. Um I've been working in the cloud native AI space for the last seven years or so now. Hello. And uh I'm Royal Alex. I work for IBM research something like 25 years. Started with IBM middleware. After that uh cloud infrastructure, cloud solutions and currently my focus on data processing automation. And um today we'll be talking to you about um foundation data foundation model data engineering uh using kubernetes. So to give a brief overview of the agenda uh we'll be introducing what data what these data processing workflows look like first then we'll talk about how projects such as cube ray and cubeflow pipelines can be used to scale up and productionize your workflows. Then we'll kick off the demo and then introduce another project called um data preparation kit which makes it much easier to build these systems out. Okay. So let's talk about data prep-processing workflows. The for work workflows usually starts from data corpse access and in our case we use paret files with error tables format and uh when we work with large data sets duplication or semi-duplications are often present and uh therefore the first uh steps in the data processing it's uh working with the dduplication which can be exact duplication or combination of exact ract or fit duplication.

After that usually or might be language separation and filtering which allows to proceed with next steps based on a specific language. Depends on uh the data input. Some annotated transformers can exist for example to check that data doesn't include personal identifiable information PII or hate abuse profanity language or just uh check that quality of documents. This transforms at least in our case there are mutual uh they do do not depends one to another and we can execute them uh in any order or even in parallel because they write data in separate uh columns. We will see that in the next slide. And usually the process ends with filtering and tokenization. Like I said before, the one some uh steps can can run in parallel and merge at the end. Another type of parallelism can be applied based on natural language because after uh and we're going to demonstrate it in demo after language separation uh all next steps can be run independently and execute uh for each language. So um as Alexi talked about right like you have lots of pre-processing stages in your pipeline.

These stages may or may not be li
