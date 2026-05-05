---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data"]
speakers: ["Dan Sun", "Bloomberg", "Theofilos Papapanagiotou", "Amazon"]
sched_url: https://kccnceu2023.sched.com/event/1HyeE/the-state-and-future-of-cloud-native-model-serving-dan-sun-bloomberg-theofilos-papapanagiotou-amazon
youtube_search_url: https://www.youtube.com/results?search_query=The+State+and+Future+of+Cloud-Native+Model+Serving+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The State and Future of Cloud-Native Model Serving - Dan Sun, Bloomberg & Theofilos Papapanagiotou, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Dan Sun, Bloomberg, Theofilos Papapanagiotou, Amazon
- Schedule: https://kccnceu2023.sched.com/event/1HyeE/the-state-and-future-of-cloud-native-model-serving-dan-sun-bloomberg-theofilos-papapanagiotou-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=The+State+and+Future+of+Cloud-Native+Model+Serving+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The State and Future of Cloud-Native Model Serving.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyeE/the-state-and-future-of-cloud-native-model-serving-dan-sun-bloomberg-theofilos-papapanagiotou-amazon
- YouTube search: https://www.youtube.com/results?search_query=The+State+and+Future+of+Cloud-Native+Model+Serving+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=s6TDq8naG48
- YouTube title: KServe: The State and Future of Cloud Native Model Serving (Kubeflow Summit 2022)
- Match score: 0.781
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-state-and-future-of-cloud-native-model-serving/s6TDq8naG48.txt
- Transcript chars: 17796
- Keywords: inference, serving, models, mesh, support, server, runtime, deploy, protocol, format, deployment, features, another, runtimes, storage, introduced, serverless, production

### Resumo baseado na transcript

yeah so today uh um you're going to present the case of uh the state and the future of the uh Cloud native model serving um so my name is Dan uh I lead the Emir inference team at Bloomberg and Nick is uh um with IBM Nikki want to introduce yourself um hi yeah I um I work for IBM in Watson Core Group um we uh maintain sort of common ml infrastructure components for different products and uh young contribute to queso cool um yeah so uh the

### Excerpt da transcript

yeah so today uh um you're going to present the case of uh the state and the future of the uh Cloud native model serving um so my name is Dan uh I lead the Emir inference team at Bloomberg and Nick is uh um with IBM Nikki want to introduce yourself um hi yeah I um I work for IBM in Watson Core Group um we uh maintain sort of common ml infrastructure components for different products and uh young contribute to queso cool um yeah so uh the case of was our main primary Creed to solve the challenging model deployment issue online kubernetes so deploying models on kubernetes uh it's not a very difficulty problem uh so um user have to learn like model theorizations and how to build model servers and uh understand the HTTP grpc protocol how to continualize the model server uh and you need to know all the kubernetes concepts like deployment service like how do you like Auto scale your like art departments with HPA vpa or like um kpia and in order to keep the uh the service um here also you want to know like set up like a written is your driving is props and then all these like in order to secure service you need to understand like a service mesh and uh um open the time like um nowadays like the models are getting bigger and bigger and over the time they're serving the models and CPUs are no longer can set for your latency requirements so you'll need to reserve your models on gpus to reduce latency so um so as you can see like a deploying models on like homeless it has a um you need to learn a lot and besides your data science like a skill set um so um all so cases like we initially create a caser mainly to address and this uh these challenges like we want to like make the deployment really easy and um we just want to if user can give us a model then we can easily turn it into a HTTP endpoint user can call easily to encapsulate all these like infrastructure details um so yeah so case server is a highly scalable and a standards based serverless model inference platform um on kubernetes um that encompasses all the complexity um deploying models to production and now the project um Personnel is now hosted in as an incubation project in Fai data Foundation um and so we moved to the Fai early this year um yeah so um the case of can be deployed as a standalone or you can also deploy case server as an add-on component with Q flow on any cloud or on-prem um so yeah some states about the case surf um right now we have around like based on the latest surveys uh there are 60
