---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Data Processing + Storage"
themes: ["Storage Data"]
speakers: ["Shubham Pampattiwar", "Scott Seago", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2CW53/snapshots-gone-wild-taming-multi-pvc-chaos-with-volumegroupsnapshot-shubham-pampattiwar-scott-seago-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Snapshots+Gone+Wild%3A+Taming+Multi-PVC+Chaos+with+VolumeGroupSnapshot+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Snapshots Gone Wild: Taming Multi-PVC Chaos with VolumeGroupSnapshot - Shubham Pampattiwar & Scott Seago, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Shubham Pampattiwar, Scott Seago, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2CW53/snapshots-gone-wild-taming-multi-pvc-chaos-with-volumegroupsnapshot-shubham-pampattiwar-scott-seago-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Snapshots+Gone+Wild%3A+Taming+Multi-PVC+Chaos+with+VolumeGroupSnapshot+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Snapshots Gone Wild: Taming Multi-PVC Chaos with VolumeGroupSnapshot.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW53/snapshots-gone-wild-taming-multi-pvc-chaos-with-volumegroupsnapshot-shubham-pampattiwar-scott-seago-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Snapshots+Gone+Wild%3A+Taming+Multi-PVC+Chaos+with+VolumeGroupSnapshot+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=pLmRkRO6O6E
- YouTube title: Snapshots Gone Wild: Taming Multi-PVC Chaos with VolumeGroupSna... Shubham Pampattiwar & Scott Seago
- Match score: 0.9
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/snapshots-gone-wild-taming-multi-pvc-chaos-with-volumegroupsnapshot/pLmRkRO6O6E.txt
- Transcript chars: 22784
- Keywords: volume, snapshot, snapshots, backup, valero, restore, individual, application, driver, consistency, cluster, create, storage, content, volumes, atomic, grouping, everything

### Resumo baseado na transcript

Um, how many of you have bagged up a multi-olume stateful application and prayed that the restore would work? Uh, today we are going to show you why those prayers were necessary and how volume group snapshot solves it. Uh then I'll show you how we brought volume group snapshots into Valero and the design decisions that we took and the implementation aspects. So the problem uh think about a database application uh like Postgra SQL, MongoDB, Cassandra, anything. So this is the norm for um any serious stateful workload deployed on Kubernetes today like uh databases it could be analytics pipelines or message cues. Uh database with write logs out of sync um you'll see corruption the right side log references data that doesn't exist.

### Excerpt da transcript

Hello everyone. Um, how many of you have bagged up a multi-olume stateful application and prayed that the restore would work? Yeah. So, us too. And that's what this talk is about. Uh, today we are going to show you why those prayers were necessary and how volume group snapshot solves it. Um, little bit about us. Um, I'm Shuan Pampachar. Um, principal software engineer at Red Hat. Um I work on open shift engineering team part of the open shift API for data protection product and I have been a Valero maintainer since 2022. Um and I'm Scott Sego also principal software engineer at Red Hat also a valero maintainer and a member of the open shift team. >> Okay. Uh so a quick show of hands. How many of you have used Valero? Okay. Great. Uh for those of who haven't uh Vero is a open source tool for backup, restore and disaster recovery on Kubernetes. Uh it handles everything cluster artifacts, resources, persistent volumes, scheduled backups, you name it. Uh it supports multiple uh volume backup methods uh CSI snapshots, file system backups, uh native cloud provider snapshots.

Uh but today we are focused on CSI snapshot path because that's where volume group snapshots plug in. Um, one quick announcement. Uh, Vero's CNCF sandbox application was just approved by the CNCF technical oversight committee last month. So, this is a great moment for us in the project. Thank you. >> Yeah. And before starting uh just like to say that we like to think backup should be simple, reliable and ideally so boring that they never make headlines. So, let's get into it. So this is going to be our road map for today. Um we'll start with why multi volume backups break. Then Scott will walk you through volume group snapshot API the community's answer that solves this. Uh then I'll show you how we brought volume group snapshots into Valero and the design decisions that we took and the implementation aspects. Uh then Scott will share some war stories from real CSI drivers testing like how things broke in ways we didn't expect. and we'll close with some results, benchmarks, and a blueprint for adopting volume group snapshots in your environment.

So the problem uh think about a database application uh like Postgra SQL, MongoDB, Cassandra, anything. So they typically spread data across volumes like you have got your data volume with table and indices. Uh you have a writer head log volume. uh you have a config volume with certificates and settings. So in this example there are three PVCs uh t
