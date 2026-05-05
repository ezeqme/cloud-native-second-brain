---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Networking + Edge + Telco"
themes: ["Networking", "Storage Data"]
speakers: ["Siyuan Zhang", "Google", "Bogdan Kanivets", "Apple"]
sched_url: https://kccnceu2024.sched.com/event/1YeSz/unleash-the-power-of-etcd-what-can-an-extensible-etcd-bring-siyuan-zhang-google-bogdan-kanivets-apple
youtube_search_url: https://www.youtube.com/results?search_query=Unleash+the+Power+of+etcd%3A+What+Can+an+E%5BXtensible%5D-etcd+Bring%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Unleash the Power of etcd: What Can an E[Xtensible]-etcd Bring? - Siyuan Zhang, Google & Bogdan Kanivets, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[Storage Data]]
- País/cidade: France / Paris
- Speakers: Siyuan Zhang, Google, Bogdan Kanivets, Apple
- Schedule: https://kccnceu2024.sched.com/event/1YeSz/unleash-the-power-of-etcd-what-can-an-extensible-etcd-bring-siyuan-zhang-google-bogdan-kanivets-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Unleash+the+Power+of+etcd%3A+What+Can+an+E%5BXtensible%5D-etcd+Bring%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Unleash the Power of etcd: What Can an E[Xtensible]-etcd Bring?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSz/unleash-the-power-of-etcd-what-can-an-extensible-etcd-bring-siyuan-zhang-google-bogdan-kanivets-apple
- YouTube search: https://www.youtube.com/results?search_query=Unleash+the+Power+of+etcd%3A+What+Can+an+E%5BXtensible%5D-etcd+Bring%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VL9111ony2k
- YouTube title: Unleash the Power of etcd: What Can an E[Xtensible]-etcd Bring? - Siyuan Zhang & Bogdan Kanivets
- Match score: 0.885
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/unleash-the-power-of-etcd-what-can-an-e-xtensible-etcd-bring/VL9111ony2k.txt
- Transcript chars: 16724
- Keywords: memory, performance, badger, database, values, sqlite, benchmark, backends, requirements, actually, interesting, systems, second, extensible, backend, basically, revisions, little

### Resumo baseado na transcript

uh hi good afternoon uh uh thank you for showing up for the last talk of this cucon uh so my name isan and I'm working as a software engineer from Google and I'm bden I'm a software engineer at Apple uh so today we're going to talk about uh Unleash the Power of SCD uh the potentials and constraints of an extensible uh ACD so the the idea of this talk is so we all know that SD uses uh bbo as its uh persistence uh storage but we're

### Excerpt da transcript

uh hi good afternoon uh uh thank you for showing up for the last talk of this cucon uh so my name isan and I'm working as a software engineer from Google and I'm bden I'm a software engineer at Apple uh so today we're going to talk about uh Unleash the Power of SCD uh the potentials and constraints of an extensible uh ACD so the the idea of this talk is so we all know that SD uses uh bbo as its uh persistence uh storage but we're just wondering um why and uh could it be something else so uh this talk is just uh entertaining this idea of maybe we should make the back end ofd more extensible and try something else uh so in this talk we'll cover some uh background knowledge and then uh introduce how we uh on our side how we extend the that back ACD backend and then uh we'll share some results of uh The Benchmark performance of three backends we have tried and then uh dive deep into the CPU and memoral memory profiling of these three backends okay okay so initially we're going to go through some background knowledge for those people who are new to ATD or don't work on the CD all their day um so here's the so ETD is the uh strongly consistent key value store and uh uh it uses raft um to achieve that strong consistency so a lot of ETD architecture is around draft um and uh since it's a key Value Store it also has its own mvcc implementation that is backed by embedded uh bold DB or bolt uh database uh and then also a lot of logic uh in NCD is dealing with peer communication uh which is also part of raft so let's uh look at the uh typical right flow which is on the leader um so the main I'm not going to go through all the uh numbers but one thing I'm going to I want to really focus on is to Showcase that uh there are two streams of work there's that number three persistence uh to transaction to wall which is basically uh right into right Ahad log and uh that's a requirement uh uh that is coming from ra and then there's also uh a right to the mvcc backand that uh then asynchronously will write to the B bolt so MCC stands for multiversion concurrency control and basically it gives us history of the revisions of the uh uh Keys let's look at also a typical uh read flow so this one is simpler uh we don't need to write any of course like writing this into wall but we still need to um make sure that uh we are reading the correct index so that's why there is that get read index uh but most of the work is done on the mvcc layer and uh that's where we get our key values um
