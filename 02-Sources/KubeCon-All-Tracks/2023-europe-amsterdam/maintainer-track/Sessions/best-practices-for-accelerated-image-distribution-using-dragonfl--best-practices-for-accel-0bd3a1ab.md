---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Wenbo Qi", "Ant Group", "Yiyang Huang", "ByteDance"]
sched_url: https://kccnceu2023.sched.com/event/1HyXt/best-practices-for-accelerated-image-distribution-using-dragonfly-wenbo-qi-ant-group-yiyang-huang-bytedance
youtube_search_url: https://www.youtube.com/results?search_query=Best+Practices+for+Accelerated+Image+Distribution+Using+Dragonfly+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Best Practices for Accelerated Image Distribution Using Dragonfly - Wenbo Qi, Ant Group & Yiyang Huang, ByteDance

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Wenbo Qi, Ant Group, Yiyang Huang, ByteDance
- Schedule: https://kccnceu2023.sched.com/event/1HyXt/best-practices-for-accelerated-image-distribution-using-dragonfly-wenbo-qi-ant-group-yiyang-huang-bytedance
- Busca YouTube: https://www.youtube.com/results?search_query=Best+Practices+for+Accelerated+Image+Distribution+Using+Dragonfly+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Best Practices for Accelerated Image Distribution Using Dragonfly.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyXt/best-practices-for-accelerated-image-distribution-using-dragonfly-wenbo-qi-ant-group-yiyang-huang-bytedance
- YouTube search: https://www.youtube.com/results?search_query=Best+Practices+for+Accelerated+Image+Distribution+Using+Dragonfly+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8zhX6306Nno
- YouTube title: Best Practices for Accelerated Image Distribution Using Dragonfly - Wenbo Qi & Yiyang Huang
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/best-practices-for-accelerated-image-distribution-using-dragonfly/8zhX6306Nno.txt
- Transcript chars: 16552
- Keywords: download, container, another, dragonfly, source, manager, cluster, traffic, engine, scheduler, bandwidth, distribution, provides, control, modules, images, acceleration, include

### Resumo baseado na transcript

hello everyone the topic of this part is the best practice for Accelerated image distribution using dragonfly there are two speakers working as a maintainer for dragonfly at the old group and my partner Ian Huang from bad things who is also a maintainer for dragonfly first let's introduce the jungflight project and some other research and development date in the past year jump fly is an open source P2P based file system under image acceleration system it's hosted by Cloud native Computing Foundation as a incubating live project its

### Excerpt da transcript

hello everyone the topic of this part is the best practice for Accelerated image distribution using dragonfly there are two speakers working as a maintainer for dragonfly at the old group and my partner Ian Huang from bad things who is also a maintainer for dragonfly first let's introduce the jungflight project and some other research and development date in the past year jump fly is an open source P2P based file system under image acceleration system it's hosted by Cloud native Computing Foundation as a incubating live project its designs to improve the physical and the speed of large-scale field distribution is used on the fields of the application distribution touch distribution log distribution and image distribution at this stage some flight has abled based on drum fly 1 on the base of maintaining the core capabilities of GameFly 1.fly it has been upgraded in major features such as system architecture design product capabilities film fly has been selected and put into production used by many internet companies since it open source in 2017 and the inter inter-sensive in October 2018.

in 2020 since I've TLC voted to accept John fly as a sense of incubating project termfly has developed developed the next version through production protects which is observed the advantage of John fly 1 and made a lot of optimizations for non's problems now that don't fly has been released more than to 170 times the project has a table commits for a long time we can refer to the first picture which is the commit date for the passenger from flight maintenance come from different companies include ant group Alibaba patterns Baidu group get live listeners who are interested in the project can join in the community Through the link below and discuss the Feature Future development of the project with us some listeners may not know much about the jumpfly project I will introduced under architectures of the John fly project under the view of each service first drum fly consists of from forces service include managers together said peer and peer the manager in the project can be used as a manager service the scheduler in the project can be used as a scheduler service the DF team in the project can be used as a peer service under all a set peer service if they introduce each service first of all the manager service which is a Management Service is used to manage the relationship between multi-clusters or P2P cluster includes uh scheduler Caster asset pure cluster and multi peers
