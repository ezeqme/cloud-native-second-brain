---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["SRE Reliability"]
speakers: ["Keith Lucas", "David Ko", "SUSE"]
sched_url: https://kccncna2022.sched.com/event/182J5/improving-longhorn-performance-with-spdk-keith-lucas-david-ko-suse
youtube_search_url: https://www.youtube.com/results?search_query=Improving+Longhorn+Performance+With+SPDK+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Improving Longhorn Performance With SPDK - Keith Lucas & David Ko, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Keith Lucas, David Ko, SUSE
- Schedule: https://kccncna2022.sched.com/event/182J5/improving-longhorn-performance-with-spdk-keith-lucas-david-ko-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Improving+Longhorn+Performance+With+SPDK+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Improving Longhorn Performance With SPDK.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182J5/improving-longhorn-performance-with-spdk-keith-lucas-david-ko-suse
- YouTube search: https://www.youtube.com/results?search_query=Improving+Longhorn+Performance+With+SPDK+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ve-wXQZNjlg
- YouTube title: Improving Longhorn Performance With SPDK - Keith Lucas & David Ko, SUSE
- Match score: 0.835
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/improving-longhorn-performance-with-spdk/ve-wXQZNjlg.txt
- Transcript chars: 24258
- Keywords: longhorn, engine, volume, better, performance, process, support, device, replicas, equivalent, basically, sparse, kernel, volumes, currently, fabrics, protocol, current

### Resumo baseado na transcript

uh so yeah uh welcome everyone and today we will talk about how to improve a long home based on spdk so I'm David Koh uh from Susan I'm Keith Lucas from Oracle labs so we just guessed up yeah probably someone uh in this room probably did not use long before so we have a one part we'll talk about what is a long home and what a longhorn walks and how to try to challenge long has right now and next we will talk about based on the

### Excerpt da transcript

uh so yeah uh welcome everyone and today we will talk about how to improve a long home based on spdk so I'm David Koh uh from Susan I'm Keith Lucas from Oracle labs so we just guessed up yeah probably someone uh in this room probably did not use long before so we have a one part we'll talk about what is a long home and what a longhorn walks and how to try to challenge long has right now and next we will talk about based on the challenging we are facing right now how we leverage spdk in the future and how it really works and what benefit you will be tagged from spdk and lastly we will talk about our Benchmark we have right now to share with everyone and also some areas want to improve in the future okay so uh long uh long is a CNC project incubating uh project right now and he's a focused on the persistent voting stuff so it's highly available and software-defined uh persistent bus storage based on kubernetes and also wrong for kubernetes so all the things we just leverage on the kubernetes stuff so he's quite lightweight reliable and easy to use what I say that because we based on the user experience and we don't have any external dependence actually so take example we don't have any external database or stuff we just leverage the kubernetes resource like API resource so this is what we have so deploy logo is quite simple and also we support all the persistent voting and with the different type of volume modes SS modes rewrite many rewrite only as a multimoice bar device Software System L of course if you use a long haul you will question about rewrite many is it when you will get to uh General Virgo so you can check it tomorrow we have another session a maintenance track talk about local roadmap and also it's a storage agnostic so let me he will be easy to deploy based on the host the whole file system any five stands for the specifier because uh Longhorns are used the sports file for his simple Vision capability so uh here we mentioned the esd4 and xfs is actually verified by longontin so you can use that directly and also not just in cluster we have inclusive snapshot but also support external backup and restore so uh different type of backup Target we support right now is NFS and S3 compatible API the pickup Target and as I say the kubernetes I will use the kubernetes resource so kubernetes design patency while we adopt our basically control patterns and customer resource design sorry yeah definition is what we use right now and also it's open source a
