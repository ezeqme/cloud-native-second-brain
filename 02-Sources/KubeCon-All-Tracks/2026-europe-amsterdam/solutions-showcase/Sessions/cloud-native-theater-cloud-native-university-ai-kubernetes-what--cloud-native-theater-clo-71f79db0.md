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
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Michael Forrester", "KodeKloud"]
sched_url: https://kccnceu2026.sched.com/event/2EG0V/cloud-native-theater-cloud-native-university-ai-+-kubernetes-what-beginners-need-to-know-in-2026-michael-forrester-kodekloud
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+AI+%2B+Kubernetes%3A+What+Beginners+Need+to+Know+in+2026+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Cloud Native University: AI + Kubernetes: What Beginners Need to Know in 2026 - Michael Forrester, KodeKloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Michael Forrester, KodeKloud
- Schedule: https://kccnceu2026.sched.com/event/2EG0V/cloud-native-theater-cloud-native-university-ai-+-kubernetes-what-beginners-need-to-know-in-2026-michael-forrester-kodekloud
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+AI+%2B+Kubernetes%3A+What+Beginners+Need+to+Know+in+2026+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Cloud Native University: AI + Kubernetes: What Beginners Need to Know in 2026.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0V/cloud-native-theater-cloud-native-university-ai-+-kubernetes-what-beginners-need-to-know-in-2026-michael-forrester-kodekloud
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Cloud+Native+University%3A+AI+%2B+Kubernetes%3A+What+Beginners+Need+to+Know+in+2026+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FdBkGi08SI4
- YouTube title: Cloud Native Theater | Cloud Native University: AI + Kubernetes: What Beginners... Michael Forrester
- Match score: 0.912
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-cloud-native-university-ai-kubernetes-what-beginn/FdBkGi08SI4.txt
- Transcript chars: 15350
- Keywords: native, already, training, models, workloads, scheduling, agents, whatever, question, bottom, workload, foundation, existing, features, either, little, gateway, probably

### Resumo baseado na transcript

Um, just want to mention that uh seems like maybe people are interested in this topic. There's a lot in the wings here and I just want to say that um I'm going to cover a very narrow opinionated set of things because as you know there's a broad ecosystem already of operator aligned AI that we could talk about. I think we could argue that Kubernetes is one of those existing platforms by far. So just from a Kubernetes perspective, what is Kubernetes doing to make it like prepare it for AI workloads? So, learning how the existing systems are evolving to handle AI workloads is absolutely solid. So bottom line is is that DRA was added into Kubernetes along with other features like in place pod resize which you just if you were here 30 minutes ago Mungshot and I were just talking about how to figure out where that came from

### Excerpt da transcript

in a world where only AI No, I'm just kidding. Would that be great if I had like a a trailer for this? Um, just want to mention that uh seems like maybe people are interested in this topic. There's a lot in the wings here and I just want to say that um I'm going to cover a very narrow opinionated set of things because as you know there's a broad ecosystem already of operator aligned AI that we could talk about. So let's get into it. All right, just a quick statement because you know sometimes we tell a story and sometimes we throw statistics at you so we can melt your brains before we get into the story. Um, so just know is like there's a bunch of statistics that talk about how people are are not training as much as they used to. I mean like why would you? I mean do you really need to? And then I I sometimes get the argument where people are like but but we like we have special needs like we have special focus domains that we need to to like focus on like finance or healthcare or whatever. But just so you know, at least in the latest research papers, generally trained models will outperform narrowly trained models easily, right?

They'll do a better job in a narrow domain than a specifically trained model, right? Just as an example. The reason I share this is because people are not rolling their own as much as you think they would be, right? They're taking existing models and running them on existing platforms. I think we could argue that Kubernetes is one of those existing platforms by far. So just from a Kubernetes perspective, what is Kubernetes doing to make it like prepare it for AI workloads? Well, you saw the keynote this morning. Nvidia, right? Nvidia has been contributing to this space has a part of it. They've added features such as DRRA, right? Which allows you basically to not just assign GPUs, but also to fractionate them and add different characteristics to the GPUs, right? So you can say, I want this driver version, right? I want this much memory. I want this kind of characteristic in the GPU. So, if you were like a beginner and you're like, "Michael, how am I going to keep my job?" Which, by the way, is literally a question I got yesterday from both an 18-year-old and from a like who was just starting and a 30-year veteran.

It's interesting that both young and old are kind of like, "How am I going to either get or keep my job in 2026?" Well, before you panic, I just want to say that this is not the first time something disruptive has come
