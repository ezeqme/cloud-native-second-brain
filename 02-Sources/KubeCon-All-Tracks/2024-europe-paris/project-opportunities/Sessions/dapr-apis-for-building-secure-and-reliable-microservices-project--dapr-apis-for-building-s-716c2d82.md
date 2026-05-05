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
themes: ["Security"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQXP/dapr-apis-for-building-secure-and-reliable-microservices-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Dapr%3A+APIs+for+building+secure+and+reliable+microservices+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Dapr: APIs for building secure and reliable microservices | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Security]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQXP/dapr-apis-for-building-secure-and-reliable-microservices-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Dapr%3A+APIs+for+building+secure+and+reliable+microservices+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Dapr: APIs for building secure and reliable microservices | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQXP/dapr-apis-for-building-secure-and-reliable-microservices-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Dapr%3A+APIs+for+building+secure+and+reliable+microservices+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Lwm4yThV9DA
- YouTube title: Dapr: APIs for building secure and reliable microservices | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/dapr-apis-for-building-secure-and-reliable-microservices-project-light/Lwm4yThV9DA.txt
- Transcript chars: 7016
- Keywords: application, instance, message, definitely, across, development, discord, workflow, authoring, reliable, microservices, depper, distributed, another, servic, resiliency, website, please

### Resumo baseado na transcript

all right ready to go hi everyone I'm Mark derer one of the depper community managers and of course I'm here to talk about deer maybe some of you guess it already with with this head uh at Deer is very useful for apis for building secure and reliable microservices so let's set a bit of context first so U if you're building dist distributed applications that involve many microservices and different kind of state stores and different kind of message Brokers um then you run into some kind of

### Excerpt da transcript

all right ready to go hi everyone I'm Mark derer one of the depper community managers and of course I'm here to talk about deer maybe some of you guess it already with with this head uh at Deer is very useful for apis for building secure and reliable microservices so let's set a bit of context first so U if you're building dist distributed applications that involve many microservices and different kind of state stores and different kind of message Brokers um then you run into some kind of developer challenges right because you always have to think about certain things one of these things is how you like proper service orchestration right so how can you make like calls across different services in a reliable way um how do you do like distributed tracing across services and also across message Brokers another thing is how do you do like Access Control right so how do you define which servers can call which other service which servic is allowed to um um save some state to your database and which servic is allowed to publish on a topic for instance um and finally how do you deal with resiliency because yeah some things will always fail U maybe some servic are not available temporarily or maybe a Stage store is unavailable for for a moment so how do you do then how do you do re rise for instance so if you're in this situation then deer the distribute application runtime is really something for you on the right you see our our newly designed website definitely have have a look there later on um deer runs in a side car so it uses the side car pattern and the side car takes care of the heavy lifting so you just ride your business logic in any language that you that you want in your application and the deer sidec will take care of the secur the observability and the resiliency so if you look from deer from development to hosting you can basically use any language to talk to the deer side car because the Deer Side Car accepts like calls via HTTP or drpc we also have a couple of uh client sdks as well so if you prefer to use a client SDK please please go for that and deer offers like a very broad Suite of different apis that really speeds up microservice development one of the newer ones is workflows you can now write your workflows in code and do like service orchestration via workflows and we also have like a pop sub API a service appication API State Management you can do like the actoral and so on and so on and with each release of deer and this this API service
