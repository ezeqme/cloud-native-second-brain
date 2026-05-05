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
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Aarno Aukia", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFwg/project-lightning-talk-cncf-sandbox-project-k8up-under-the-hood-aarno-aukia-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CNCF+Sandbox+Project+K8Up+Under+The+Hood+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: CNCF Sandbox Project K8Up Under The Hood - Aarno Aukia, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Aarno Aukia, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFwg/project-lightning-talk-cncf-sandbox-project-k8up-under-the-hood-aarno-aukia-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CNCF+Sandbox+Project+K8Up+Under+The+Hood+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: CNCF Sandbox Project K8Up Under The Hood.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFwg/project-lightning-talk-cncf-sandbox-project-k8up-under-the-hood-aarno-aukia-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CNCF+Sandbox+Project+K8Up+Under+The+Hood+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NtXvB9gWTu8
- YouTube title: Project Lightning Talk: CNCF Sandbox Project K8Up Under The Hood - Aarno Aukia, Maintainer
- Match score: 0.926
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-cncf-sandbox-project-k8up-under-the-hood/NtXvB9gWTu8.txt
- Transcript chars: 5699
- Keywords: backup, restore, course, actually, whatever, backups, availability, sandbox, started, important, multiple, distributed, whether, operator, backed, cluster, applications, restic

### Resumo baseado na transcript

Uh when I started using Kubernetes in 20 late 2015 um of course boost it did mostly for like stateless apps. So I mean the data it was mostly for mural right but I mean I guess we're at CubeCon but even outside of of this bubble uh more and more people are using Kubernetes to actually host uh important workload with important data. have query anymore and thus the whole service went down for a few hours until they had the fire put out and the the power put back on. as a operator make the backups and then when it breaks when it goes up in flames you restore the data right but the problem there's some problems with that right first one is which data should you back up and how often right usually it be backed up, what are the security requirements and all of that because of course the application people know that about their applications. state with the cluster um we use uh a battleproven uh open source backup tool called restic um that's been around for way longer than we have we're just auler and the kubernetes packaging around that um and of course believing in githops we believe

### Excerpt da transcript

So I'm one of the maintainers of the KUP CNCF sandbox project. Uh when I started using Kubernetes in 20 late 2015 um of course boost it did mostly for like stateless apps. So I mean the data it was mostly for mural right but I mean I guess we're at CubeCon but even outside of of this bubble uh more and more people are using Kubernetes to actually host uh important workload with important data. Now you might have an idea that you know something bad can happen to your data right uh unless you make you think about you know making more and more more replicas and stuff. you distribute your uh your nodes under multiple racks or multiple availability zones and then you wake up one morning and you discover that all your racks you distributed on were actually stacked one on top of each other and when the lowest started burning all the others went up in smoke as well as happened um uh actually not that far from here. The other one is it actually built three different data centers in one major region. uh they distributed all the nodes on uh on the different availability zones and then they woke up one morning and discovered oops I don't know whether it was an accident or the labeling was off or whatever the the incident that the postmortem doesn't say they discovered that actually the nodes weren't distributed like regularly all over all the availability zones the majority of the nodes happened to be in the same availability zone and of course it was the one that went offline and thus um they didn't have query anymore and thus the whole service went down for a few hours until they had the fire put out and the the power put back on.

So you see when you have this kind of you know life happens when you have these kind of incidents um there um it would make sense to uh make backups right and that's how we started um to develop um kap the backup operator in 2018 um and we had there already then there were some other uh backup operators out there some of them even open source and then you know backed by community project but most of them were making backups from the infrastructure side right you as a operator make the backups and then when it breaks when it goes up in flames you restore the data right but the problem there's some problems with that right first one is which data should you back up and how often right usually you as the operator you don't really know that right there might be multiple workloads running on there you don't know their restore point objectives
