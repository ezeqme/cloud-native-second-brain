---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Keynote Sessions"
themes: ["AI ML", "SRE Reliability", "Sustainability"]
speakers: ["Lu Qiu", "Alluxio", "Susan Wu", "Clayton Coleman", "Google", "Peter Pouliout", "Ampere Computing", "Ricardo Rocha", "CERN"]
sched_url: https://kccnceu2024.sched.com/event/1YhIO/keynote-panel-discussion-optimizing-performance-and-sustainability-for-ai-lu-qiu-alluxio-susan-wu-clayton-coleman-google-peter-pouliout-ampere-computing-ricardo-rocha-cern
youtube_search_url: https://www.youtube.com/results?search_query=Keynote+Panel+Discussion%3A+Optimizing+Performance+and+Sustainability+for+AI+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Keynote Panel Discussion: Optimizing Performance and Sustainability for AI - Lu Qiu, Alluxio; Susan Wu & Clayton Coleman, Google; Peter Pouliout, Ampere Computing; Ricardo Rocha, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Sustainability]]
- País/cidade: France / Paris
- Speakers: Lu Qiu, Alluxio, Susan Wu, Clayton Coleman, Google, Peter Pouliout, Ampere Computing, Ricardo Rocha, CERN
- Schedule: https://kccnceu2024.sched.com/event/1YhIO/keynote-panel-discussion-optimizing-performance-and-sustainability-for-ai-lu-qiu-alluxio-susan-wu-clayton-coleman-google-peter-pouliout-ampere-computing-ricardo-rocha-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote+Panel+Discussion%3A+Optimizing+Performance+and+Sustainability+for+AI+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Keynote Panel Discussion: Optimizing Performance and Sustainability for AI.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YhIO/keynote-panel-discussion-optimizing-performance-and-sustainability-for-ai-lu-qiu-alluxio-susan-wu-clayton-coleman-google-peter-pouliout-ampere-computing-ricardo-rocha-cern
- YouTube search: https://www.youtube.com/results?search_query=Keynote+Panel+Discussion%3A+Optimizing+Performance+and+Sustainability+for+AI+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VcMOr1DtTWM
- YouTube title: Keynote Panel Discussion: Optimizing Performance and Sustainability for AI
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/keynote-panel-discussion-optimizing-performance-and-sustainability-for/VcMOr1DtTWM.txt
- Transcript chars: 13350
- Keywords: workloads, gpu, running, performance, better, actually, approach, utilization, resources, ricardo, source, together, inference, compute, llm, talked, clayton, computing

### Resumo baseado na transcript

hi everyone my name is Susan woo I'm in outbound product management in Google Cloud um I'm here with my friends and colleagues I'm going to let them introduce themselves hi I'm uh Clayton Coleman I'm really excited this year I can finally claim that I have a 10 plus years uh experience in kubernetes so that's going straight on my resume and hopefully I'll be uh hirable someplace Peter pul Amper Computing it's a pleasure to be here in Paris this week great to see everybody looking forward to

### Excerpt da transcript

hi everyone my name is Susan woo I'm in outbound product management in Google Cloud um I'm here with my friends and colleagues I'm going to let them introduce themselves hi I'm uh Clayton Coleman I'm really excited this year I can finally claim that I have a 10 plus years uh experience in kubernetes so that's going straight on my resume and hopefully I'll be uh hirable someplace Peter pul Amper Computing it's a pleasure to be here in Paris this week great to see everybody looking forward to a a F week talking about kubernetes and Cloud native I'm Ricardo um I'm Computing engineer at CERN I'm also part of the TOC and the tab in the cncf really happy to be here meet everyone hi I'm Lou so I'm the PNC maintainer of the open source project called alasil and hopefully I can see like how we dat Ai and kubernetes work together in kcom okay Clayton ready I guess so Enterprises are building a lot of AI platforms on kubernetes and I hear platform operators talk about um abstracting kubernetes for from the data Sciences um what can we do to make kubernetes simpler oh my gosh what can't we do to make kubernetes um so it's interesting um data scientists don't need to know about kubernetes but there's a bunch of things that their platform teams are going to need uh and I think I I can simplify by saying uh kubernetes is supposed to be a cluster uh or uh operating system and the job of an operating system is to abstract Hardware so you heard from Kevin there's a bunch of exciting work going on uh in a number of sigs and kubernetes around abstracting the resource model making accelerators easier to uh run um but making just the details that the platform admins need exposed up above that um that's going to lead to better opportunities for scheduling and Bin packing uh for putting uh keeping those really really really expensive accelerators working and uh the point of kubernetes has always been to run multiple workloads together and that's actually what helps a lot of people achieve significant efficiency so on top of those uh accelerators and a better resource model we really do need uh to bring batch Frameworks like slurm and Ray uh closer to kubernetes we need to be able to support them effectively and then uh finally since you know training is really just the development part of the process everybody's got to go to production at some point and I think kubernetes needs to be the best place um to run production inference workloads and so the focus I think will have to be
