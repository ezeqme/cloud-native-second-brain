---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Derek Wang", "Vigith Maurice", "Intuit"]
sched_url: https://kccnceu2024.sched.com/event/1YeNl/empowering-developers-with-easy-scalable-stream-processing-technologies-on-kubernetes-derek-wang-vigith-maurice-intuit
youtube_search_url: https://www.youtube.com/results?search_query=Empowering+Developers+with+Easy%2C+Scalable+Stream+Processing+Technologies+on+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Empowering Developers with Easy, Scalable Stream Processing Technologies on Kubernetes - Derek Wang & Vigith Maurice, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Derek Wang, Vigith Maurice, Intuit
- Schedule: https://kccnceu2024.sched.com/event/1YeNl/empowering-developers-with-easy-scalable-stream-processing-technologies-on-kubernetes-derek-wang-vigith-maurice-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=Empowering+Developers+with+Easy%2C+Scalable+Stream+Processing+Technologies+on+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Empowering Developers with Easy, Scalable Stream Processing Technologies on Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeNl/empowering-developers-with-easy-scalable-stream-processing-technologies-on-kubernetes-derek-wang-vigith-maurice-intuit
- YouTube search: https://www.youtube.com/results?search_query=Empowering+Developers+with+Easy%2C+Scalable+Stream+Processing+Technologies+on+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_JyHHTFXUeA
- YouTube title: Empowering Developers with Easy, Scalable Stream Processing Technologies on Kubernetes
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/empowering-developers-with-easy-scalable-stream-processing-technologie/_JyHHTFXUeA.txt
- Transcript chars: 35231
- Keywords: actually, source, pipeline, processing, streaming, stream, platform, support, running, write, information, question, process, machine, learning, native, aggregation, enrichment

### Resumo baseado na transcript

good afternoon everyone welcome welcome welcome to kcon and thanks for coming into my talk today we're going to talk about something interesting about streaming data processing my name is Derek W my body BJ marus is supposed to be here but he has some last minute change cannot make it both vet and I are principal Engineers working for in and we are the Project Lead or open source project nma flow I personally also the project leader or cncf graduate project ARG events here's today's agenda we're going

### Excerpt da transcript

good afternoon everyone welcome welcome welcome to kcon and thanks for coming into my talk today we're going to talk about something interesting about streaming data processing my name is Derek W my body BJ marus is supposed to be here but he has some last minute change cannot make it both vet and I are principal Engineers working for in and we are the Project Lead or open source project nma flow I personally also the project leader or cncf graduate project ARG events here's today's agenda we're going to start with a brief introduction about our employer into it and then we're going to talk about stream data processing its benefits in use cases and we're also going to talk about the challenges we experienced when we use streaming technology with our system platforms and then give our resolutions our open source project nlow followed by demo and then in the end I'm going to take questions start with the introduction about int I'm not sure how familiar you guys are with the int the int is a a well-known fintech company which is based in North America because we have some very famous product turu P Karma QuickBooks and melin the turx is the most popular uh tax returning folling tool almost everyone knows about it in North America and all these major products are actually powered by our five key platform areas these five key platform areas make sure we deliver value to our customers and Accel Innovations consistently across our organizations and with 100% of our service running on kubernetes based modern s platform we are enabling billions of machine learning predictions to billions Dollar's movement across our systems with the secure and smart approach inter is also very large open source Community player we do not only use open source technology build our platforms bu our services we also contribute a lot to open source Community as many of you know in is a creator of Argo which is one of the most popular cncf graduate project we also got two time cncf and user award in 2019 22 and more than that we actually open source a lot of projects some of are listed here and the one we're going to talk about today is called Numa flow which is a c native stream data processing platform the one with a PO icon okay um finishing all these introductions let's move on to talk about stream data processing before doing that I would like to ask you some questions how many of you actually um data Engineers or ever working on data processing if you don't mind can raise your hand
