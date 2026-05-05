---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Matthias Bertschy", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2Es7x/project-lightning-talk-scaling-kubescape-to-thousands-of-nodes-matthias-bertschy-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scaling+Kubescape+to+Thousands+of+Nodes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Scaling Kubescape to Thousands of Nodes - Matthias Bertschy, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Matthias Bertschy, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2Es7x/project-lightning-talk-scaling-kubescape-to-thousands-of-nodes-matthias-bertschy-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scaling+Kubescape+to+Thousands+of+Nodes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Scaling Kubescape to Thousands of Nodes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2Es7x/project-lightning-talk-scaling-kubescape-to-thousands-of-nodes-matthias-bertschy-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Scaling+Kubescape+to+Thousands+of+Nodes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=abVrry6PQdQ
- YouTube title: Project Lightning Talk: Scaling Kubescape to Thousands of Nodes - Matthias Bertschy, Maintainer
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-scaling-kubescape-to-thousands-of-nodes/abVrry6PQdQ.txt
- Transcript chars: 3860
- Keywords: storage, server, thousands, profiles, update, object, create, method, sending, objects, container, cubecape, runtime, second, aggregated, standard, minutes, attempt

### Resumo baseado na transcript

So what happens when you are really proud of your project and then you deploy it to a very large cluster? Well, this is what happened when we tried to handle 5,000 nodes and each node sending 10 megabyte objects for each container running periodically. Uh the problem is when you have uh different replicas or even more like demon sets, you have 5,000 node agents sending the same data at the same time and you have a lock contention and uh you create also a lot of of back So when you send that patch suddenly in the storage you only have 30 seconds to read the big object from the disk unmarshall it apply the patch and save it back and then if you have also uh mutexes to make sure you don't update the same object it doesn't work. So third attempt that's the current one we moved the intelligent to the storage layer instead. So with this decoupled right path uh we were allowed it enabled us to to scale much better.

### Excerpt da transcript

Hi everybody. I'm Matias. I'm a maintainer of Cubscape. So what happens when you are really proud of your project and then you deploy it to a very large cluster? Well, this is what happened when we tried to handle 5,000 nodes and each node sending 10 megabyte objects for each container running periodically. What you end up with is a thundering herd which I tried to represent here. And uh my talk is the story on how we hit a wall where lock contentions from thousands of nodes made the traditional Kubernetes storage patterns obsolete and how we rebuilt the cubescape architecture to survive it. So let me talk about cube cubecape a little bit. So it's a comprehensive CNCF security platform for Kubernetes. We are an incubating project and we provide continuous scanning and deep ebpf runtime observability and this data is used to do to create second profiles network policies but also uh runtime detection using the CL language and we can send alerts to alert manager or the sys log. And this depths of of data generates a lot a lot of data.

So and this data we store them in what we call container profiles and a single profiles is easily tens of megabytes. And when you have like thousands of nodes continuously update this data at massive scale uh it creates uh a problem with the API server logic. So with such big big objects we cannot use etc. So we are we have our own aggregated API server and every node agent sends the learn profiles uh to this storage and the other components they are consuming this data via the standard Kubernetes API. Um so at first it was a very naive approach. We said okay each node agent keeps in memory the entire CRD and like every 10 minutes we just send the full object to persist it uh using the create method. It doesn't work. Uh the problem is when you have uh different replicas or even more like demon sets, you have 5,000 node agents sending the same data at the same time and you have a lock contention and uh you create also a lot of of back and forth traffic because when you have a conflict you get back the object that you need to update you update it and you send it again.

So it's it's horrible. So second attempt we tried uh the patch method. So every node agent like for for the the 10 minutes they generate a JSON patch and then they send it and they rely on the aggregated API server to apply this patch. The problem is this. So this is also a standard method of the API server but it is also synchronous. So when you send that patch s
