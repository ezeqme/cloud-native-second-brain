---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Leon Chang", "Oppo"]
sched_url: https://kccncna2022.sched.com/event/182QR/the-evolution-and-innovation-of-cubefs-leon-chang-oppo
youtube_search_url: https://www.youtube.com/results?search_query=The+Evolution+and+Innovation+of+CubeFS+CNCF+KubeCon+2022
slides: []
status: parsed
---

# The Evolution and Innovation of CubeFS - Leon Chang, Oppo

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Leon Chang, Oppo
- Schedule: https://kccncna2022.sched.com/event/182QR/the-evolution-and-innovation-of-cubefs-leon-chang-oppo
- Busca YouTube: https://www.youtube.com/results?search_query=The+Evolution+and+Innovation+of+CubeFS+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre The Evolution and Innovation of CubeFS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182QR/the-evolution-and-innovation-of-cubefs-leon-chang-oppo
- YouTube search: https://www.youtube.com/results?search_query=The+Evolution+and+Innovation+of+CubeFS+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rcCzTj61jNU
- YouTube title: The Evolution and Innovation of CubeFS - Leon Chang, Oppo
- Match score: 0.906
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/the-evolution-and-innovation-of-cubefs/rcCzTj61jNU.txt
- Transcript chars: 20843
- Keywords: storage, reduce, gpu, second, cost, performance, shuffle, public, subsystem, version, advice, stability, multiple, training, computing, single, coding, management

### Resumo baseado na transcript

hello everyone I'm living Chang coming from story team of Oppo and I am the main tuner of Cuba fast product it's my great honor to introduce Cuba advice today open source in March 2019 released version 1.0 at April at the end of 2019 with John Cena box in 2020 we updated several times and supported divorce interfaces including S3 and AP advice in 2021 released version 2.4 which enhanced the stability at the beginning of this year we released version 3 which is a significant release support usual

### Excerpt da transcript

hello everyone I'm living Chang coming from story team of Oppo and I am the main tuner of Cuba fast product it's my great honor to introduce Cuba advice today open source in March 2019 released version 1.0 at April at the end of 2019 with John Cena box in 2020 we updated several times and supported divorce interfaces including S3 and AP advice in 2021 released version 2.4 which enhanced the stability at the beginning of this year we released version 3 which is a significant release support usual code report to reduce the cost in the scenarios as the trick and hradp online for one year in our previous storage platform they are honored that the Cuba has become an incubation project future and in August we will release the Virgin we already released the Virgin uh 3.1 which is supposed to have read the cloud acceleration and Qs flow control components in terms of Open Source Community groups We compare the dates before and after joining the sandbox the increasing numbers indicates that cubas increase the Impractical applications many software Engineers are willing to join and contribute to the product and many end users likely to make tests or use in production environment in the field of storage some technical changes are commonly acknowledged to obstruct critical applications for example we have to deal with files from KB to TB most small it's hard to use read write patterns sequentially or randomly of course there are many more difficulties than this this on the beam Point pinpoint of marriage management mentioned before supervised probably so extensible magic systems now I know the story is segmented by region and performance is fully persistent to memory so that shot and without pipelines in ensure strong consistency between methods copies the figure shows the management organization of the shares in the magic the B3 is used to manage the entry and I know and the features such as copy on right are Implement which is combined for operations such as modifications which make essential persistence the entire index design is relatively sophisticated compared with the product so friends that this design can better solve the problem of supportability and strong consistency we will talk about supporting multiple water literature and it's mainly implements in these two phase one is for the entry and another is foreign storing small files centrally in storage nodes to stream moving the small files to one big file which can improve the sort of output and performance
