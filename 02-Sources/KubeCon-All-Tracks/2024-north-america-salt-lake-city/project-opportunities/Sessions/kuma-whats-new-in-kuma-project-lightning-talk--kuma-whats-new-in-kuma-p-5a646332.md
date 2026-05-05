---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW9T/kuma-whats-new-in-kuma-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Kuma%3A+What%E2%80%99s+New+in+Kuma%3F+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Kuma: What’s New in Kuma? | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW9T/kuma-whats-new-in-kuma-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Kuma%3A+What%E2%80%99s+New+in+Kuma%3F+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Kuma: What’s New in Kuma? | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW9T/kuma-whats-new-in-kuma-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Kuma%3A+What%E2%80%99s+New+in+Kuma%3F+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=52A593Kxo8Y
- YouTube title: Kuma: What’s New in Kuma? | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/kuma-whats-new-in-kuma-project-lightning-talk/52A593Kxo8Y.txt
- Transcript chars: 3801
- Keywords: policies, mesh, multiple, features, namespace, create, default, external, advanced, running, version, around, timeout, producer, clients, seconds, consumer, configuration

### Resumo baseado na transcript

okay hello everyone I am Christopher and I am an engineer uh working on the Open Source service mesh called Kuma uh I'm a bit jet loed but I'm excited to talk to you folks uh so let's get started uh for those of you that never heard about Kuma uh it is a service mesh and it does all of the service meshy stuff that you would expect uh like security observability Advanced rounding resiliency and so on uh in addition to that we do our best to try

### Excerpt da transcript

okay hello everyone I am Christopher and I am an engineer uh working on the Open Source service mesh called Kuma uh I'm a bit jet loed but I'm excited to talk to you folks uh so let's get started uh for those of you that never heard about Kuma uh it is a service mesh and it does all of the service meshy stuff that you would expect uh like security observability Advanced rounding resiliency and so on uh in addition to that we do our best to try to make it very easy for you to run in multiple clouds in multiple clusters and even run multiple mesches inside one Kuma installation we also try to make the experience of running Kuma on kubernetes um the same as running on VM so it's really similar and it's easy for you and um we try to make it very easy for you to use all of the advanced features of envoy uh that being said we've just released version 2.9.0 like last week and we really happy about that there there are numerous uh improvements in there and some new features like MH TLS uh MH Services namespace policies and we also have a GUI that comes out of the box and we um continue to modernize the GUI and to work on features there uh as you can see this is the data plane view on the right side that was recently implemented there all right so let's dive into it um namespace policies so up until 2.9 uh the policies in Kuma were Global and now uh We've made them namespaced so if you want to play around with something like a retry or a timeout or anything like that uh you can basically create a namespace then appli apply those policies in the Nam space and when you're done and you remove the name space everything is cleaned up and you don't have to worry about like leaving stuff around and we have two types of uh of those Nam space policies one of them is a producer policy and those are the policies that are in the same uh Nam space as the target resource uh and this is mostly for like the creators of apis to give um the clients of your apis sensible defaults so if I create an API and I know that a good default for a timeout would be 5 seconds then by default all of the clients will get uh that five uh that five seconds and there are also consumer policies and these are policies that are created on the same Nam space as the client so if I want to uh for if I know that I want to retry uh request to this particular API five times instead of the two times that are the default I can do that and uh as a consequence of that the the configuration of consumer policies ov
