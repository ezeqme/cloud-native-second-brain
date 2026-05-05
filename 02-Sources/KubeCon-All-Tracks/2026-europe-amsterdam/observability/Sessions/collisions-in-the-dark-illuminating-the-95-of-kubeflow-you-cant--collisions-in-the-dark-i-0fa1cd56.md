---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Observability"
themes: ["Observability"]
speakers: ["Amine Lahouel", "Laura Llinares", "CERN"]
sched_url: https://kccnceu2026.sched.com/event/2CW6t/collisions-in-the-dark-illuminating-the-95-of-kubeflow-you-cant-see-amine-lahouel-laura-llinares-cern
youtube_search_url: https://www.youtube.com/results?search_query=Collisions+in+the+Dark%3A+Illuminating+the+95%25+of+Kubeflow+You+Can%27t+See+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Collisions in the Dark: Illuminating the 95% of Kubeflow You Can't See - Amine Lahouel & Laura Llinares, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Amine Lahouel, Laura Llinares, CERN
- Schedule: https://kccnceu2026.sched.com/event/2CW6t/collisions-in-the-dark-illuminating-the-95-of-kubeflow-you-cant-see-amine-lahouel-laura-llinares-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Collisions+in+the+Dark%3A+Illuminating+the+95%25+of+Kubeflow+You+Can%27t+See+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Collisions in the Dark: Illuminating the 95% of Kubeflow You Can't See.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6t/collisions-in-the-dark-illuminating-the-95-of-kubeflow-you-cant-see-amine-lahouel-laura-llinares-cern
- YouTube search: https://www.youtube.com/results?search_query=Collisions+in+the+Dark%3A+Illuminating+the+95%25+of+Kubeflow+You+Can%27t+See+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AsPCWEBiR6g
- YouTube title: Collisions in the Dark: Illuminating the 95% of Kubeflow You Can't... Amine Lahouel & Laura Llinares
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/collisions-in-the-dark-illuminating-the-95-of-kubeflow-you-cant-see/AsPCWEBiR6g.txt
- Transcript chars: 19863
- Keywords: metrics, little, energy, gpu, cluster, hardware, dashboard, workloads, running, monitoring, exporters, everything, wanted, platform, metics, memory, prometheus, software

### Resumo baseado na transcript

Uh hello and uh welcome everybody for our talk uh collision in the dark. I forgot I'm eliminating the 95% of Kuflow that you cannot see and this will talk will explain a little bit our observability stock that we are using. Then this data is sent to tape for storage and all the scientific they do their analysis on it. So we design procure deploy and operate the hardware and software platforms that we will be supporting. Um yes so one of the software platform we have a scientific computing platform that we build uh for machine learning and it's based on cubeflow and some other promising open source component. uh we provide access to a shared pool of resources of GPU and compute units and this can be interactive but you can also uh it's used also for job submission and we have we have a focus on machine learning workload and yesterday I

### Excerpt da transcript

Uh hello and uh welcome everybody for our talk uh collision in the dark. I forgot I'm eliminating the 95% of Kuflow that you cannot see and this will talk will explain a little bit our observability stock that we are using. Oh, I Oh, pop I didn't. So, first uh myself, I will present myself. I am I mean Lel software engineer at CERN and I have nearly uh one decade of experience and >> and you saw it already but I'm Lara. I'm 25 years old and I'm a DevOps engineer at CERN as well. >> So, do you hear me? I think yes. So before we go into the technical detail we wanted to present a bit briefly what is CERN and what is the context of all the project. So Cers CERN is the biggest um high energy physics laboratory. It's famous for the discovery of the of the bosen and this discovery was enabled because of the large collider that we have below the swans and the French and Swiss border. This collider has as you can see on the picture many experiment that are collecting a huge amount of collision data. So those collision happens up to 40 million times per second.

So this is a lot of data. So because there's a lot of data we have to and we only care about rare and interesting event to discover new physics. Uh they use something called the trigger system. So what is it? It's um what you see here on the slide. We have the level one trigger trigger that is hardware based and we filter this 40 millions uh collision data per second and we'll uh filter around 99% of it and all this data will then go to the level two triggers which is software based and same this second layer will also filter around 99% of the data. Then this data is sent to tape for storage and all the scientific they do their analysis on it. Uh so then we are now in what it's called run free. Uh and we will move to something called I luminosity LHC which mean luminosity means more data. So if you want even more data you need more better trigger system and that's how the project NGT which is next generation triggers came into the picture. So it's a research and de development initiative. Uh and it's focusing on this data acquisition and this trigger system and a real-time event processing and in our team especially we are working on the scientific computing infrastructure of NGT.

So we design procure deploy and operate the hardware and software platforms that we will be supporting. Um yes so one of the software platform we have a scientific computing platform that we build uh for machine learning and it's
