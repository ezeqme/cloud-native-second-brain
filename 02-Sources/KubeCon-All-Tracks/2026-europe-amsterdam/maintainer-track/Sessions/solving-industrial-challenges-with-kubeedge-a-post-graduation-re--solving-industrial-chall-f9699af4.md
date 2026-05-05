---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Yue Bao", "Huawei", "Hongbing Zhang", "DaoCloud", "Yin Ding", "VMware by Broadcom"]
sched_url: https://kccnceu2026.sched.com/event/2EF3u/solving-industrial-challenges-with-kubeedge-a-post-graduation-report-yue-bao-huawei-hongbing-zhang-daocloud-yin-ding-vmware-by-broadcom
youtube_search_url: https://www.youtube.com/results?search_query=Solving+Industrial+Challenges+With+KubeEdge%3A+A+Post-Graduation+Report+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Solving Industrial Challenges With KubeEdge: A Post-Graduation Report - Yue Bao, Huawei; Hongbing Zhang, DaoCloud; Yin Ding, VMware by Broadcom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Yue Bao, Huawei, Hongbing Zhang, DaoCloud, Yin Ding, VMware by Broadcom
- Schedule: https://kccnceu2026.sched.com/event/2EF3u/solving-industrial-challenges-with-kubeedge-a-post-graduation-report-yue-bao-huawei-hongbing-zhang-daocloud-yin-ding-vmware-by-broadcom
- Busca YouTube: https://www.youtube.com/results?search_query=Solving+Industrial+Challenges+With+KubeEdge%3A+A+Post-Graduation+Report+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Solving Industrial Challenges With KubeEdge: A Post-Graduation Report.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF3u/solving-industrial-challenges-with-kubeedge-a-post-graduation-report-yue-bao-huawei-hongbing-zhang-daocloud-yin-ding-vmware-by-broadcom
- YouTube search: https://www.youtube.com/results?search_query=Solving+Industrial+Challenges+With+KubeEdge%3A+A+Post-Graduation+Report+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uYxY04HJI0w
- YouTube title: Solving Industrial Challenges With KubeEdge: A Post-Graduation... Yue Bao, Hongbing Zhang & Yin Ding
- Match score: 0.875
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/solving-industrial-challenges-with-kubeedge-a-post-graduation-report/uYxY04HJI0w.txt
- Transcript chars: 18009
- Keywords: result, inference, device, scenarios, graduated, control, robots, learning, customer, pretty, running, typical, devices, industry, keynote, basically, scenario, deploy

### Resumo baseado na transcript

Our today's topic will focus on solving the industry challenge with Kubage. So, this one we're focusing on the recent AI focusing and also a lot of a case study. So we solved the problem from the cloud and edge there's a long latency a date connection is not reliable data privacy all these things we try to solve by uh cloud edge code coordination problem by kub edge basically the basic idea was just So this we uh support all the main stream of AI frameworks including tensor, pyarch, pedal pedal from bu and man scope man and so we support uh joint inference increment learning federated learning I will go a little bit detail on this one and So for uh thing is we call it feder federated learning is different from uh the traditional traditional u combined learning. So we can have a edge side learning and we aggregate all the intermediate result back to the cloud to consolidate uh based on the inter each individual training result.

### Excerpt da transcript

Hi, welcome to our maintenance track. Our today's topic will focus on solving the industry challenge with Kubage. So, uh we our project graduated on 2024. So, this one we're focusing on the recent AI focusing and also a lot of a case study. So, uh this is my colleague uh Honging. He is a TSA member. My name is Inding. I also a TSC member of uh Kuba edge. So we started uh this this project about 10 years ago. So it's a long journey. I would like to share our journey with you guys today. So first uh you can see in uh keynote yesterday uh we our project are very honored. So it's mentioned this good slider is behind the kubit deployment. So it's based on kuba deployment. This a our sixth time we are on the kubcon keynote. So very excited notes. Uh thank you everyone. So we are really excited to power industry user cases behind by our kovage project. So uh we are a innovated project journey. I will skimmed it. So it's back to 2018. We are part of a uh Kubernetes IoT work group. We launched it on the November 2018.

Then we donate this project to CNL Foundation on 2019 uh March. And it's a long journey. We uh become a became a uh incubation project in 2020. Then uh we finally graduated on 2024 October is on Chicago is Chicago Detroit uh is Chicago Kubakong. It's finally we graduate as a the first graduation project on the cloud native edge. So no other in the CNF blueprint there's no other edge project graded. So we were the first one. So I will quickly introduce our K edge basically is we want to use the Kubernetes control plane to help solve the cloud edge coordination pro uh the problems. So usually this case is different because u it's cloud edge the deployment scenario is different from pure data center deployment. So we solved the problem from the cloud and edge there's a long latency a date connection is not reliable data privacy all these things we try to solve by uh cloud edge code coordination problem by kub edge basically the basic idea was just deploy the control plane on the cloud and deploy not the traditional kuballet not the cloud the worker node not in the cloud but in the edge side.

So from cloud edge we set up a new duplex the two communication channel to secure cloud edge communication and the uh synchronization and also we are solving the uh long latency issues and the unreliable connection. So if the connection interrupted, we can restore the edge node back to the desired state controlled by the control plane. So uh currently we have more
