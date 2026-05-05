---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Manish Gill", "ClickHouse Inc"]
sched_url: https://kccnceu2024.sched.com/event/1YePt/fantastic-ordinals-and-how-to-avoid-them-auto-scaling-challenges-in-a-cloud-database-manish-gill-clickhouse-inc
youtube_search_url: https://www.youtube.com/results?search_query=Fantastic+Ordinals+and+How+to+Avoid+Them%3A+Auto-Scaling+Challenges+in+a+Cloud+Database+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Fantastic Ordinals and How to Avoid Them: Auto-Scaling Challenges in a Cloud Database - Manish Gill, ClickHouse Inc

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Manish Gill, ClickHouse Inc
- Schedule: https://kccnceu2024.sched.com/event/1YePt/fantastic-ordinals-and-how-to-avoid-them-auto-scaling-challenges-in-a-cloud-database-manish-gill-clickhouse-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Fantastic+Ordinals+and+How+to+Avoid+Them%3A+Auto-Scaling+Challenges+in+a+Cloud+Database+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Fantastic Ordinals and How to Avoid Them: Auto-Scaling Challenges in a Cloud Database.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YePt/fantastic-ordinals-and-how-to-avoid-them-auto-scaling-challenges-in-a-cloud-database-manish-gill-clickhouse-inc
- YouTube search: https://www.youtube.com/results?search_query=Fantastic+Ordinals+and+How+to+Avoid+Them%3A+Auto-Scaling+Challenges+in+a+Cloud+Database+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=AFoMsLMZKik
- YouTube title: Fantastic Ordinals and How to Avoid Them: Auto-Scaling Challenges in a Cloud Database
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/fantastic-ordinals-and-how-to-avoid-them-auto-scaling-challenges-in-a/AFoMsLMZKik.txt
- Transcript chars: 35581
- Keywords: actually, stateful, scaling, replicas, replica, inside, vertical, operator, controller, always, ordinals, database, delete, running, happens, wanted, arbitrary, topology

### Resumo baseado na transcript

all right I think we can get started so hi everyone welcome to this talk uh it's titled fantastic ordinals and how to avoid them Autos scaling challenges in a cloud database uh my name is Manish Gil and I work for a company called click house so I'm an engineering manager at click house uh I work in a team which is the scale team and the primary thing we do at click house is think about vertical and horizontal Auto scaling uh idling scaling to zero and we

### Excerpt da transcript

all right I think we can get started so hi everyone welcome to this talk uh it's titled fantastic ordinals and how to avoid them Autos scaling challenges in a cloud database uh my name is Manish Gil and I work for a company called click house so I'm an engineering manager at click house uh I work in a team which is the scale team and the primary thing we do at click house is think about vertical and horizontal Auto scaling uh idling scaling to zero and we also heavily contribute to the click house operator in order to facilitate uh the scaling mechanics so this is the agenda for today we're going to look at click house the technology uh we're going to talk about click house Cloud we're going to talk about the auto scaling architecture of uh click house we're going to look at vertical scaling specifically as a problem that we faced in Click house and then uh what the models of vertical scaling are specifically what we call the break first model of scaling uh then we're going to go into something we like to call make before break as an alternative approach uh we're going to look at some uh like uh some nuances of how stateful sets work and the limitations of stateful set and how are how we dealt with the problems okay so click house click house itself uh I don't know probably some people are familiar with it it's an open- Source column oriented database it's a distributed olab database specifically so the workloads that click house typically runs are analytic analytical nature uh it's got a reputation as being a really really fast uh database so most of the times like you'll see people running click house clusters with like uh terabytes to terabytes of magnitude and yeah it's uh feel free to Google it it's a pretty powerful Tool uh for the purpose of our talk what's important is it's a distributed multimaster database and it's eventually consistent and so whenever I'm talking about like pots or or replicas in Click house uh there is no such concept of a primary with like a repli repli in turn so all replicas can ingest traffic and all of the replicas can serve query so like no one replica is special here so click house cloud is our serverless offering uh of Click house uh we try to uh make uh give you like a fully managed experience you don't have to like deploy your own shared nothing architectures uh it's serverless it's got ideling and autoscaling and that's what my team is responsible for it's also got separation of compute and storage so the storage in
