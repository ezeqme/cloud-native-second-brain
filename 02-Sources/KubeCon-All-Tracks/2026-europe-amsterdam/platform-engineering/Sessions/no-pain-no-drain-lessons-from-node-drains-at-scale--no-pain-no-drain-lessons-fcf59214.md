---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering", "SRE Reliability"]
speakers: ["Ryan Hallisey", "Natalie Bandel", "NVIDIA"]
sched_url: https://kccnceu2026.sched.com/event/2CVxq/no-pain-no-drain-lessons-from-node-drains-at-scale-ryan-hallisey-natalie-bandel-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=No+Pain+No+Drain%3A+Lessons+From+Node+Drains+at+Scale+CNCF+KubeCon+2026
slides: []
status: parsed
---

# No Pain No Drain: Lessons From Node Drains at Scale - Ryan Hallisey & Natalie Bandel, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ryan Hallisey, Natalie Bandel, NVIDIA
- Schedule: https://kccnceu2026.sched.com/event/2CVxq/no-pain-no-drain-lessons-from-node-drains-at-scale-ryan-hallisey-natalie-bandel-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=No+Pain+No+Drain%3A+Lessons+From+Node+Drains+at+Scale+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre No Pain No Drain: Lessons From Node Drains at Scale.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVxq/no-pain-no-drain-lessons-from-node-drains-at-scale-ryan-hallisey-natalie-bandel-nvidia
- YouTube search: https://www.youtube.com/results?search_query=No+Pain+No+Drain%3A+Lessons+From+Node+Drains+at+Scale+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=E7HIwOHbeN8
- YouTube title: No Pain No Drain: Lessons From Node Drains at Scale - Ryan Hallisey & Natalie Bandel, NVIDIA
- Match score: 0.815
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/no-pain-no-drain-lessons-from-node-drains-at-scale/E7HIwOHbeN8.txt
- Transcript chars: 26185
- Keywords: maintenance, process, little, workloads, important, drains, workload, actually, states, specific, maintenances, solution, trying, controller, management, gpu, started, another

### Resumo baseado na transcript

We're from Nvidia and uh before we dive into the details of our talk, I want to share a little bit about uh what what we experience uh maintaining our infrastructure and our team has experienced. These life cycle events would hurt our overall capacity in our fleet and they would hurt our sanity. The problem so I talked about uh uh drain this so this is and and and sort of go back to the beginning of the story for us is that we started with cube cut drain. Uh but there are some challenges when you start here and first of all just a context set about cube drain. And so like what comes to mind immediately is like well if you're doing drain why not think about where to do drain right we're trying to improve the operational cost we're trying to increase the uptime of our of our GPUs let's think about And so as you as you start from that cube cut drain we this is something that you will quickly learn and evolve to.

### Excerpt da transcript

Okay. Hi everybody. I'm Ryan Haly and I'm joined by my colleague Natalie Vanell. We're from Nvidia and uh before we dive into the details of our talk, I want to share a little bit about uh what what we experience uh maintaining our infrastructure and our team has experienced. So in a single day we will do about a thousand node drains. a thousand no drains. Three years ago, we would do almost zero. It was a manual process for us. And we would experience all these life cycle events every single day. Things like device failures, driver failures. These life cycle events would hurt our overall capacity in our fleet and they would hurt our sanity. And so we never really liked experiencing these things. And we wanted to come up with a solution, something that made our lives better. And so that's what this talk's about. It's a talk about a journey. It's about a story um about all the work that went into going from a manual life cycle management process, a manual train process to a fully automated seamless solution.

And uh so we're going to go through that story. Okay, first uh I I love having a picture to kind of kick things off. I kind of feel for this this person and the the crane operator. This is like I can identify with this this person. This is like what drain's like if you wanted to do drain manually. This is like how I would feel. There's a lot of crates falling everywhere. You kind of need to figure out the how to control the the chaos that that you're experiencing. Okay. So um the scale what's the context for for all the things that we're doing. So at Nvidia we will uh we run thousands of GPUs uh in our data centers. Our workload is a game streaming workload. It's a latency sensitive workload. It is uh it's ephemeral. It has a an SLA to it meaning like it will terminate after a certain amount of time. has a maximum timeout to it. Uh we do lots of planned maintenances. We do lots of unplanned maintenances, actually even more unplanned maintenances than we do planned maintenance. And uh drain has a cost to it.

Has an operational cost. And that cost is GPU hours. And our goal is how do we minimize that? How do we minimize the cost of of doing drain? ically maximize the amount of GPU hours uh that we are using uh we're giving to our customers. Okay. The problem so I talked about uh uh drain this so this is and and and sort of go back to the beginning of the story for us is that we started with cube cut drain. This is how it all began. That's probably how e
