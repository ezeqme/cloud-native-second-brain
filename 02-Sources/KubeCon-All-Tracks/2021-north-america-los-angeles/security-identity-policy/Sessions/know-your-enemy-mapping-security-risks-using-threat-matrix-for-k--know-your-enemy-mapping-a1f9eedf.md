---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Yossi Weizman", "Ram Pliskin", "Microsoft"]
sched_url: https://kccncna2021.sched.com/event/lV3M/know-your-enemy-mapping-security-risks-using-threat-matrix-for-kubernetes-yossi-weizman-ram-pliskin-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Know+Your+Enemy%3A+Mapping+Security+Risks+Using+Threat+Matrix+for+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Know Your Enemy: Mapping Security Risks Using Threat Matrix for Kubernetes - Yossi Weizman & Ram Pliskin, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Yossi Weizman, Ram Pliskin, Microsoft
- Schedule: https://kccncna2021.sched.com/event/lV3M/know-your-enemy-mapping-security-risks-using-threat-matrix-for-kubernetes-yossi-weizman-ram-pliskin-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Know+Your+Enemy%3A+Mapping+Security+Risks+Using+Threat+Matrix+for+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Know Your Enemy: Mapping Security Risks Using Threat Matrix for Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV3M/know-your-enemy-mapping-security-risks-using-threat-matrix-for-kubernetes-yossi-weizman-ram-pliskin-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Know+Your+Enemy%3A+Mapping+Security+Risks+Using+Threat+Matrix+for+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=JTwiNGzr3wM
- YouTube title: Know Your Enemy: Mapping Security Risks Using Threat Matrix for Kuber... Yossi Weizman & Ram Pliskin
- Match score: 0.918
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/know-your-enemy-mapping-security-risks-using-threat-matrix-for-kuberne/JTwiNGzr3wM.txt
- Transcript chars: 16712
- Keywords: metrics, container, containers, attack, attackers, security, monitor, access, threat, techniques, identity, images, cluster, threats, exposed, dashboard, matrix, microsoft

### Resumo baseado na transcript

hello everyone i'm josie weisman a senior security researcher at microsoft and with me is ron pliskin a principal security resource manager at microsoft we will talk in this session about the threat metrics to kubernetes which is a knowledge base of the security threats that target kubernetes this metrics is one of the first attempts to systematically map the threats of kubernetes and we will see how we can use it to improve the security of our environments and measure our security coverage to potential attacks ram will start

### Excerpt da transcript

hello everyone i'm josie weisman a senior security researcher at microsoft and with me is ron pliskin a principal security resource manager at microsoft we will talk in this session about the threat metrics to kubernetes which is a knowledge base of the security threats that target kubernetes this metrics is one of the first attempts to systematically map the threats of kubernetes and we will see how we can use it to improve the security of our environments and measure our security coverage to potential attacks ram will start with some background of this project so ram please the state is yours hi everyone i'm ram i'm leading the security research team for azure defender at microsoft please allow me to outline what you're expected to get from today's talk first we will introduce the problem space and what led us to focus on the orchestration layer for containers second the throat metrics for kubernetes this is the outcome of our research of kubernetes strength landscape we will also go over an attack we witnessed and we will unfold it using the metrics then we will present an example of how organizations can leverage this knowledge base and honestly to better secure their kubernetes workloads lastly we will discuss the collaboration with folks from mitre to establish mitral support for containers we will wrap up with highlighting the differences among the two matrixes to set up the stage we will start by introducing the problem space and now we got tapped into it so before kubernetes was a thing before docker was a thing folks were running distributed systems largely either on bare metal or in virtual machines when contact when containerization started to take off it provided a way for consistent and repeatable deployments with kubernetes being so widely adopted around two years back we were tasked with building a plan to protect users running kubernetes workloads that's basically how our journey started with kubernetes built as extremely robust obstruction layer we knew we would need to adjust our security perspective normally we are as we are natively integrated to azure backbone we tend to leverage any internal signal we could have to strengthen security offerings but with kubernetes being platform agnostic we aligned accordingly and shifted our focus towards the kubernetes layers let's linger for a second on the diagram in the right we split it into into three different levels starting at the bottom the cloud layer which can often be referenced as the
