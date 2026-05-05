---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Networking"]
speakers: ["Alfonso Ming and Jorge Turrado", "SCRM Lidl International Hub"]
sched_url: https://kccnceu2026.sched.com/event/2EG0t/cloud-native-theater-istio-day-the-good-the-ugly-and-the-bad-leaving-sidecars-behind-with-istio-ambient-mesh-alfonso-ming-and-jorge-turrado-scrm-lidl-international-hub
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+The+Good%2C+The+Ugly%2C+and+The+Bad%3A+Leaving+Sidecars+Behind+with+Istio+Ambient+Mesh+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Istio Day: The Good, The Ugly, and The Bad: Leaving Sidecars Behind with Istio Ambient Mesh - Alfonso Ming and Jorge Turrado, SCRM Lidl International Hub

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Alfonso Ming and Jorge Turrado, SCRM Lidl International Hub
- Schedule: https://kccnceu2026.sched.com/event/2EG0t/cloud-native-theater-istio-day-the-good-the-ugly-and-the-bad-leaving-sidecars-behind-with-istio-ambient-mesh-alfonso-ming-and-jorge-turrado-scrm-lidl-international-hub
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+The+Good%2C+The+Ugly%2C+and+The+Bad%3A+Leaving+Sidecars+Behind+with+Istio+Ambient+Mesh+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Istio Day: The Good, The Ugly, and The Bad: Leaving Sidecars Behind with Istio Ambient Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0t/cloud-native-theater-istio-day-the-good-the-ugly-and-the-bad-leaving-sidecars-behind-with-istio-ambient-mesh-alfonso-ming-and-jorge-turrado-scrm-lidl-international-hub
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+The+Good%2C+The+Ugly%2C+and+The+Bad%3A+Leaving+Sidecars+Behind+with+Istio+Ambient+Mesh+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ToKv7JntLvY
- YouTube title: Cloud Native Theater | Istio Day: The Good, The Ugly, and The Bad... Alfonso Ming and Jorge Turrado
- Match score: 0.804
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-istio-day-the-good-the-ugly-and-the-bad-leaving-s/ToKv7JntLvY.txt
- Transcript chars: 23897
- Keywords: waypoint, traffic, tunnel, proxies, policies, ambient, gateway, another, metrics, amount, running, cost, cluster, complex, thanks, approach, cannot, warload

### Resumo baseado na transcript

And there are my achievements GADA CNCF Microsoft MVP and which first of all thanks to everybody for joining us today. No, I I it's interesting where we are going to explain our adoption process of ambient mesh. So this is a model that work very fine but present at least two problems >> before before jumping to the next step everybody here knows what is this approach right? So another problem related with the CD car model is about operational complexity because if you need to uh update or some feature about the core of the you will need to restart all the balance inside the the mess. Uh when you deploy ato in ambient mess you will deploy a demon center that is called c tunnel and in this case it means that you have a c tunnel par per node. It's an API that fit really well 10 years ago, but it hasn't grow with Kubernetes in terms of features, a lot of annotation, a lot of specific inte implementation configuration that is hard to maintain.

### Excerpt da transcript

First of all, a quick introduction. >> So I am Alonso. I work in Spart. So I intend to improve the life of our teams. Happy to to stay here. >> And my name is Jorge. You can call me George if you prefer. I understand naming it's complex. Horge Turd to improve even more the spelling. I work as principal site reliability engineer at Esbar Digit. And there are my achievements GADA CNCF Microsoft MVP and which first of all thanks to everybody for joining us today. There are a lot of super interesting meetings. I hope that this meeting will be at least useful. I'm not going to commit interesting. No, I I it's interesting where we are going to explain our adoption process of ambient mesh. Erh and luckily the topic that we have chosen to to guide our session is quite aligned because I see that so many people here could request to be a risk group during the next flu campaign. So the idea is starting by a quick introduction just to ensure I'm pretty sure that all of you know what is what service me is and what gateway API is.

Sorry if not or if you are there we are going to invest five minutes just to put everybody of us in the same page to start with our uh lessons learned. So well as you know and service mesh is an uh software that works in the first layer. So can help us in order to manage our microservices and is built in this case is was built by three pillars security for the one hand observability and traffic management. So uh as uh if we are talking about security uh it provide uh authentification and uh muts for all in the all the services and if we talk about observability we can uh see and point of our in network and we can detect uh detect errors so fast. So if we talk about traffic management uh it controls the flow of data and uh lot the balance balance the load between the all the services. So >> yes sir >> yes sir. So well the first thing that we did when we introduce a service mesh in our cluster it decide about CD car model that is the standard for the last years about this or ambassar model works with a proxy every pot has a proxy and all the communications uh is between the proxies.

The proxies handle all the traffic and pass the traffic to the service A from the uh from the service A sorry to service B and all the communication and the authentification is provided by the proxies. So this is a model that work very fine but present at least two problems >> before before jumping to the next step everybody here knows what is this approach right?
