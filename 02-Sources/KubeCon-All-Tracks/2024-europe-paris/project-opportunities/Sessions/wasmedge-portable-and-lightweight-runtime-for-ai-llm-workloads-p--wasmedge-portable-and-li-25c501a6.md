---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQhz/wasmedge-portable-and-lightweight-runtime-for-aillm-workloads-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=WasmEdge%2C+portable+and+lightweight+runtime+for+AI%2FLLM+workloads+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# WasmEdge, portable and lightweight runtime for AI/LLM workloads | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQhz/wasmedge-portable-and-lightweight-runtime-for-aillm-workloads-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=WasmEdge%2C+portable+and+lightweight+runtime+for+AI%2FLLM+workloads+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre WasmEdge, portable and lightweight runtime for AI/LLM workloads | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQhz/wasmedge-portable-and-lightweight-runtime-for-aillm-workloads-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=WasmEdge%2C+portable+and+lightweight+runtime+for+AI%2FLLM+workloads+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NuLFdERpGSY
- YouTube title: WasmEdge, portable and lightweight runtime for AI/LLM workloads | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/wasmedge-portable-and-lightweight-runtime-for-ai-llm-workloads-project/NuLFdERpGSY.txt
- Transcript chars: 7146
- Keywords: application, machine, called, framework, python, gpu, portable, language, applications, compile, deploy, started, server, together, models, multiple, docker, developers

### Resumo baseado na transcript

we are the other WM project in cncf sandbox so it's really nice to have U WM Cloud pre us so you know our project is called Wasatch we also started in 2019 and we started um as a web around time outside of the browser right you know at the time a lot of people ask questions how is that different from java right you know that's because you have another bite codee um um B code virtual machine where it's cross platform provide security and all that we to build things like prompt engineering and RG framework and you know things like that into the application server so that we compile the whole L application into one piece of Deployable application and then have kubernetes to orchestrate it right you know so that is very different from the current Paradigm where you have you know multiple containers multiple python script and you know things like that but in order to do that there's a we have the problem that we we saw we have solved all those years

### Excerpt da transcript

we are the other WM project in cncf sandbox so it's really nice to have U WM Cloud pre us so you know our project is called Wasatch we also started in 2019 and we started um as a web around time outside of the browser right you know at the time a lot of people ask questions how is that different from java right you know that's because you have another bite codee um um B code virtual machine where it's cross platform provide security and all that we heard this before this is called Java right you know so um we keep fighting this perception because you know um in the cloud native space wasm is very different from java but I wouldn't go into that because in the last year uh the the the progress I want to report is that we finally find a use case that's very similar to Java and you know that's where Java had uh uh uh tremendous success but failed in the new use case which is right ones wrong anywhere but for gpus not just for CPUs using Wasa right so you know um first let me take a step back to say you know say if you are writing AI application or especially application what do you do today know so when it started you know the a application is mostly people just use uh some kind of API server that either provided by uh assas provider or open eye or you can run your own large language model using things like AMA and you know things like that ll.

CPP to start open application Ser API server and then use orchestration framework like a land chain some kind uh some python framework to tie them together and then build a uh entire application a whole chain of different models and different PS and different applications right um that is all fine however the this whole process is very much geared towards research you know um so in order for uh to really have the tighten down and highly secure and uh um you know uh uh Deployable application we need to um have applications that are much tighter tighter integrated move data and model together you know move the execution code that handles the data together with the data right you know so that means to build our own application servers like that means to build things like prompt engineering and RG framework and you know things like that into the application server so that we compile the whole L application into one piece of Deployable application and then have kubernetes to orchestrate it right you know so that is very different from the current Paradigm where you have you know multiple containers multiple python script an
