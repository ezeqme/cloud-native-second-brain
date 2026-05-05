---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["AI ML", "Observability", "Platform Engineering", "Kubernetes Core"]
speakers: ["Brett Warminski", "Gourav Khanijoe", "Hubspot"]
sched_url: https://kccncna2025.sched.com/event/27FcN/why-is-my-query-slow-real-ai-use-cases-with-vitess-+-kubernetes-+-prometheus-brett-warminski-gourav-khanijoe-hubspot
youtube_search_url: https://www.youtube.com/results?search_query=Why+Is+My+Query+Slow%3F+Real+AI+Use+Cases+With+Vitess+%2B+Kubernetes+%2B+Prometheus+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Why Is My Query Slow? Real AI Use Cases With Vitess + Kubernetes + Prometheus - Brett Warminski & Gourav Khanijoe, Hubspot

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Observability]], [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Brett Warminski, Gourav Khanijoe, Hubspot
- Schedule: https://kccncna2025.sched.com/event/27FcN/why-is-my-query-slow-real-ai-use-cases-with-vitess-+-kubernetes-+-prometheus-brett-warminski-gourav-khanijoe-hubspot
- Busca YouTube: https://www.youtube.com/results?search_query=Why+Is+My+Query+Slow%3F+Real+AI+Use+Cases+With+Vitess+%2B+Kubernetes+%2B+Prometheus+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Why Is My Query Slow? Real AI Use Cases With Vitess + Kubernetes + Prometheus.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FcN/why-is-my-query-slow-real-ai-use-cases-with-vitess-+-kubernetes-+-prometheus-brett-warminski-gourav-khanijoe-hubspot
- YouTube search: https://www.youtube.com/results?search_query=Why+Is+My+Query+Slow%3F+Real+AI+Use+Cases+With+Vitess+%2B+Kubernetes+%2B+Prometheus+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=qDBgHS2bE7s
- YouTube title: Why Is My Query Slow? Real AI Use Cases With Vitess + Kubernete... Brett Warminski & Gourav Khanijoe
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/why-is-my-query-slow-real-ai-use-cases-with-vitess-kubernetes-promethe/qDBgHS2bE7s.txt
- Transcript chars: 33503
- Keywords: actually, little, everything, started, queries, support, another, information, prompt, engineers, explain, graphana, response, talking, review, llm, weekly, workflow

### Resumo baseado na transcript

This is, as far as I can tell, the only talk about AI at the whole conference. And so, I'm really excited to have you all here uh to to hear some of the special things that uh uh that we're doing here uh at HubSpot. Here are few numbers I want to give you to to give you the sense of the scale that we are dealing with. Um and so whitus providers sharding and life cycle management and we are very heavy users of whitus and then we have a healthy dose of Prometheus Graphana and Victoria metrics just keeping eye on everything that we do. uh within data infrastructure I mean and we are supporting hundreds of product engineers right and so automation and self- service are not just nice ideas they are like the bread and butter u they're table stakes and that's the only way we scale oursel We are data infrastructure team and we support product engineers a lot of self-service tooling so that they can go and self diagn diagnose the query performance issues and any kind of operational things.

### Excerpt da transcript

Well, welcome. This is, as far as I can tell, the only talk about AI at the whole conference. And so, I'm really excited to have you all here uh to to hear some of the special things that uh uh that we're doing here uh at HubSpot. Uh the title of the talk is is why is my query slow? If if you're like us and you've been working with databases for a for a long period of time, uh this is a question that you might have been asked and what you do the next what you do immediately afterwards really changes the way that the rest of your day uh the rest of the day is going to go. Uh if you're again like us, most of the time this involves opening 18 browser tabs and sitting in a bunch of different Slack conversations trying to explain uh concepts to people who've never heard them before. uh by the time you've already looked at all the tabs and correlated all the things together and think you have an answer, the person's already gone. Uh so here we're going to tell you a little bit about how we uh about how we fixed this uh problem.

Uh so I'm Brett Winsky. I'm the uh I'm the ideas guy. This is Gorov. He's a staff engineer on the team here. We're with HubSpot. Uh we work with databases, which means we've lived through a lot of these a lot of these types of situations. And when it comes to solving uh pain points, I'm the one who comes up with the with some funny things to do. Grov actually is the one who's helped make a lot of these things happen and you'll see you'll see the results of some of his work here today. Um here's what we're going to cover. We're going to just walk you very quickly about our stack and uh how we leverage uh CNCF tooling vitess everything from the bottom all the way up. Uh then we're going to talk about three different user flows through our system. Uh two of which are for the teams that consume our stuff and one of them is a flow that we use to improve things ourselves. And at the end, I'll share some takeaways as well with some links to some uh to a future landing spot that's going to include some of this code as well because we'll open it all up.

And so without any further ado, I'll hand it over to Gar to kind of kick things off. Please enjoy. Hello, this is Goro. Thanks Brett. All right. Um let's get started. Here are few numbers I want to give you to to give you the sense of the scale that we are dealing with. And we use a lot of CNCF as you can see. Uh we got AWS and EBS handling the compute and storage. And then we have Kubernetes orc
