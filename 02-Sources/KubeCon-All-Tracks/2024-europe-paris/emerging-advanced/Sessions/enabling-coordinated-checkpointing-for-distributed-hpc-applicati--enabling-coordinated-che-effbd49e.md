---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Emerging + Advanced"
themes: ["Emerging + Advanced"]
speakers: ["Radostin Stoyanov", "University of Oxford", "Adrian Reber", "Red Hat"]
sched_url: https://kccnceu2024.sched.com/event/1YeT4/enabling-coordinated-checkpointing-for-distributed-hpc-applications-radostin-stoyanov-university-of-oxford-adrian-reber-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Enabling+Coordinated+Checkpointing+for+Distributed+HPC+Applications+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Enabling Coordinated Checkpointing for Distributed HPC Applications - Radostin Stoyanov, University of Oxford & Adrian Reber, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[Emerging + Advanced]]
- País/cidade: France / Paris
- Speakers: Radostin Stoyanov, University of Oxford, Adrian Reber, Red Hat
- Schedule: https://kccnceu2024.sched.com/event/1YeT4/enabling-coordinated-checkpointing-for-distributed-hpc-applications-radostin-stoyanov-university-of-oxford-adrian-reber-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Enabling+Coordinated+Checkpointing+for+Distributed+HPC+Applications+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Enabling Coordinated Checkpointing for Distributed HPC Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeT4/enabling-coordinated-checkpointing-for-distributed-hpc-applications-radostin-stoyanov-university-of-oxford-adrian-reber-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Enabling+Coordinated+Checkpointing+for+Distributed+HPC+Applications+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=lswkWQU4_W0
- YouTube title: Enabling Coordinated Checkpointing for Distributed HPC Applicati... Radostin Stoyanov & Adrian Reber
- Match score: 0.907
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/enabling-coordinated-checkpointing-for-distributed-hpc-applications/lswkWQU4_W0.txt
- Transcript chars: 30938
- Keywords: checkpoint, container, restore, essentially, checkpointing, containers, running, basically, question, application, applications, another, distributed, process, called, instances, working, couple

### Resumo baseado na transcript

good good afternoon Welcome to our session um distributed and enabling sorry enabling coordinated checkpointing for distributed HPC applications my name is Adan REO I work at redhead for nine years now I'm involved in um checkpoint restore which is the basis for all of what we're doing here today for 14 years now um we're doing everything we do with checkpoint restore is based on creu um I'm involved there I guess now 12 years and since I'm at redhead I'm mainly focusing on um container migration today here

### Excerpt da transcript

good good afternoon Welcome to our session um distributed and enabling sorry enabling coordinated checkpointing for distributed HPC applications my name is Adan REO I work at redhead for nine years now I'm involved in um checkpoint restore which is the basis for all of what we're doing here today for 14 years now um we're doing everything we do with checkpoint restore is based on creu um I'm involved there I guess now 12 years and since I'm at redhead I'm mainly focusing on um container migration today here with me is rtin so hello everyone my name is rtin I'm a PhD student at University of Oxford supervised by Professor West Armor and my research is focusing on enabling check restor for um HPC clusters okay and um today's agenda will look something um like this where I will go through the background of of checkpoint restore a bit about the history why the names are the way they are then I'll talk about integration into existing container run times engines orchestration then I talk about use cases why you would want to use checkpoint ReStore in combination with um containers then I will do a migration demo this is not coordinated yet it's just a simple pot migrating from one one host to another host the distance between will be about 500 kilomet and then um Rin will talk about coordinated checkpointing in an HPC environment why it's necessary and what the challenges are there so background so the tool we are using here is called creu it's called checkpoint ReStore in users space and the reason for the name especially in user space is um because it's um a tool and there were many different tools before so checkpoint restore is a technology in operating systems and Linux for a long time in in the early years 20 years ago it was mainly done in high performance Computing and the main use case was fall tolerance if you have thousand notes running something stops working you don't want to restart from the beginning So you you're looking into checkpoint restore your compute jobs regularly and at that time there were two tools developed around 20 years ago one was an external kernel module which was never inry and which you had to compile um separately to be able to use it and then you had to preload libraries so the the solution was never what you would call a transparent checkpoint because you had to prepare your application either recompile it or prepare it in some other way and to solve this problem there was um approach for checkpoint restore which was in the
