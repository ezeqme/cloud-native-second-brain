---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Emerging + Advanced"
themes: ["Kubernetes Core"]
speakers: ["Peter Hunt", "Adrian Reber", "Red Hat", "Radostin Stoyanov", "University of Oxford", "Viktória Spišaková", "Masaryk University"]
sched_url: https://kccnceu2026.sched.com/event/2CW6P/ctrl-x-ctrl-v-your-pods-wg-checkpoint-restore-in-kubernetes-peter-hunt-adrian-reber-red-hat-radostin-stoyanov-university-of-oxford-viktoria-spisakova-masaryk-university
youtube_search_url: https://www.youtube.com/results?search_query=Ctrl-X%2C+Ctrl-V+Your+Pods%3A+WG+Checkpoint+Restore+in+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Ctrl-X, Ctrl-V Your Pods: WG Checkpoint Restore in Kubernetes - Peter Hunt & Adrian Reber, Red Hat; Radostin Stoyanov, University of Oxford; Viktória Spišaková, Masaryk University

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Peter Hunt, Adrian Reber, Red Hat, Radostin Stoyanov, University of Oxford, Viktória Spišaková, Masaryk University
- Schedule: https://kccnceu2026.sched.com/event/2CW6P/ctrl-x-ctrl-v-your-pods-wg-checkpoint-restore-in-kubernetes-peter-hunt-adrian-reber-red-hat-radostin-stoyanov-university-of-oxford-viktoria-spisakova-masaryk-university
- Busca YouTube: https://www.youtube.com/results?search_query=Ctrl-X%2C+Ctrl-V+Your+Pods%3A+WG+Checkpoint+Restore+in+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Ctrl-X, Ctrl-V Your Pods: WG Checkpoint Restore in Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6P/ctrl-x-ctrl-v-your-pods-wg-checkpoint-restore-in-kubernetes-peter-hunt-adrian-reber-red-hat-radostin-stoyanov-university-of-oxford-viktoria-spisakova-masaryk-university
- YouTube search: https://www.youtube.com/results?search_query=Ctrl-X%2C+Ctrl-V+Your+Pods%3A+WG+Checkpoint+Restore+in+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lLxrtmpIlMk
- YouTube title: Ctrl-X, Ctrl-V Your Pods: WG Checkpoint Restore in Kub... Peter H, Adrian R, Radostin S & Viktória S
- Match score: 0.827
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/ctrl-x-ctrl-v-your-pods-wg-checkpoint-restore-in-kubernetes/lLxrtmpIlMk.txt
- Transcript chars: 33146
- Keywords: checkpoint, restore, essentially, checkpointing, questions, working, functionality, thinking, containers, already, migration, little, actually, useful, workloads, implementation, container, create

### Resumo baseado na transcript

Um my name is Razin and uh this in this session we are going to present the checkpoint restore working group. Um to introduce myself I'm a PhD student at University of Oxford and we have been working on the checkpoint restore functionality for several years with Adrian. Someone suggested that checkpoint restore could be really useful for like uh faster kernel security kernel upgrades. When one looks into the details and realize how complex the task is, it is perhaps unsurprising that it has taken so long and this also applies to Kubernetes. Radostian will talk more about the current state of the checkpoint restore in Kubernetes and its history but now we are here to just you know integrate it there and have it there. And so we think that it is really important to enable upstream Kubernetes native support for checkpoint restore because it will be beneficial for maybe a lot of users of upstream Kubernetes.

### Excerpt da transcript

Hello everyone. Um my name is Razin and uh this in this session we are going to present the checkpoint restore working group. Um to introduce myself I'm a PhD student at University of Oxford and we have been working on the checkpoint restore functionality for several years with Adrian. Uh unfortunately Adrian was not able to come today but uh we are going to uh cover essentially the background of the history of the project and how everything started and um Peter do you want to introduce yourself? >> Yeah. Hey everyone um my name is Peter Hunt. I'm a uh chair of Sign Node. I work at Red Hat principal software engineer and um also chair of the working group uh Checkpoint Restore. Thank you for joining. and Vicki. >> Hi everyone, I'm Victoria. I am from Maseric University in Czech Republic. And I will be also starting the whole presentation. So some of you might be asking what is even checkpoint restore? Why do I need it? Is it useful? Have I ever seen it? Maybe you haven't seen it in the context of like containers, compute, workloads or anything like that.

But I believe many of you have ever encountered these menus and you know what they're capable of. And uh usually you would use them to just like save the game and later reload the save state. Why would you do that? Well, maybe you just like uh won a hard battle or you passed some quests or you are before a hard battle or you have been playing too much and want to save the state and go to sleep and maybe like resume next day or in a couple of days and these are all use cases that are quite applicable to other workloads as well and in the context of containers. So now moving from the games to the containers. Um checkpoint restore is a quite old concept and the origins of its development and implementation date back somewhere to maybe 2005. Then over next couple of years the implementation evolved and changed and I would say that around 2010 people started to pick up on this exciting new feature that is huge. as someone said in the discussion to the one post and they started to come up with the use cases.

Um the older use cases are really interesting. Someone suggested to like turn out of memory killer into out of memory dumper. Someone suggested that checkpoint restore could be really useful for like uh faster kernel security kernel upgrades. Some people said that it's exciting for debuggers or tracers or profilers. But the use cases changed a little over time. Then next year in 2012, there was a follow up
