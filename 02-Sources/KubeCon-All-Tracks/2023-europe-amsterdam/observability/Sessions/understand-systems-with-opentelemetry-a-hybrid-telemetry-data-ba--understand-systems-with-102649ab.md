---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Observability"
themes: ["Observability", "Storage Data"]
speakers: ["Ran Xu", "Huawei", "Xiaochun Yang", "Northeastern University"]
sched_url: https://kccnceu2023.sched.com/event/1Hyb2/understand-systems-with-opentelemetry-a-hybrid-telemetry-data-backend-ran-xu-huawei-xiaochun-yang-northeastern-university
youtube_search_url: https://www.youtube.com/results?search_query=Understand+Systems+with+OpenTelemetry%3A+A+Hybrid+Telemetry+Data+Backend+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Understand Systems with OpenTelemetry: A Hybrid Telemetry Data Backend - Ran Xu, Huawei & Xiaochun Yang, Northeastern University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ran Xu, Huawei, Xiaochun Yang, Northeastern University
- Schedule: https://kccnceu2023.sched.com/event/1Hyb2/understand-systems-with-opentelemetry-a-hybrid-telemetry-data-backend-ran-xu-huawei-xiaochun-yang-northeastern-university
- Busca YouTube: https://www.youtube.com/results?search_query=Understand+Systems+with+OpenTelemetry%3A+A+Hybrid+Telemetry+Data+Backend+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Understand Systems with OpenTelemetry: A Hybrid Telemetry Data Backend.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyb2/understand-systems-with-opentelemetry-a-hybrid-telemetry-data-backend-ran-xu-huawei-xiaochun-yang-northeastern-university
- YouTube search: https://www.youtube.com/results?search_query=Understand+Systems+with+OpenTelemetry%3A+A+Hybrid+Telemetry+Data+Backend+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Zo9HVe2KUo4
- YouTube title: Understand Systems with OpenTelemetry: A Hybrid Telemetry Data Backend - Ran Xu & Xiaochun Yang
- Match score: 0.948
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/understand-systems-with-opentelemetry-a-hybrid-telemetry-data-backend/Zo9HVe2KUo4.txt
- Transcript chars: 9185
- Keywords: storage, engine, metric, gemini, introduce, logs, metrics, search, trace, backend, firstly, second, searching, circle, reduced, huawei, source, cost

### Resumo baseado na transcript

okay let's get started hello everyone I'm so excited to see some of you here and I will show you my protection named hybrid Telemetry data backend firstly let me introduce myself my name is shushan and I come from the Huawei Cloud database in the working Library and there was a co-speaker with me who's she whose name is Xiao Chen yang and she is a professor of the Northeast University in China and she has been engaged in teaching and researching in the field of data manager and

### Excerpt da transcript

okay let's get started hello everyone I'm so excited to see some of you here and I will show you my protection named hybrid Telemetry data backend firstly let me introduce myself my name is shushan and I come from the Huawei Cloud database in the working Library and there was a co-speaker with me who's she whose name is Xiao Chen yang and she is a professor of the Northeast University in China and she has been engaged in teaching and researching in the field of data manager and Analysis but I have to announce that she can't be here due to some scheduling conflict so I will step in to show her part for you okay in my team there is a open source project named open Gemini which aimed to processing the monitoring data on Huawei cloud and my presentation will departed in four four part the first is the challenge of the processing of availability data on Huawei cloud and the second is open Gemini as a back-end storage solution of open telemetry and the third I will show you some key design of the back end storage for logs and metrics and last I will show you some evaluation of our system okay there are two types of Television data on Huawei Cloud first is metric data which describes the status of the hardware and the software and is about 2 million per second and the total size is about 20 per beta per day and another is a log data is about 185 terabitha per day so this data is used for some and real-time analyzings for monitoring such as alert and normal detection temperature inside and some troubleshooting for this course we introduce a lot of data engine into our system such as spark for processing the streaming and the trade for the overlap and some time assist database to store The Matrix data and for the lost data we introduce we introduce some search engine for for text searching and the log storage it seems that it can solve some of the problems but the resultages is is also apparent firstly the message data is redundantly stored in the different storage engine so the cost of the storage must be sensitive and second different data engine has different agent and different character so we have a lot of clusters a lot of software to update and a lot of clusters to to scare out or scaling the operation cost is so expensive and last the when we want to do some correlation analysis such as joins the same Trace ID of the logs and the trace that way it's necessary to put the poor data out of the data engine and compute them and the cost of the transformation is
