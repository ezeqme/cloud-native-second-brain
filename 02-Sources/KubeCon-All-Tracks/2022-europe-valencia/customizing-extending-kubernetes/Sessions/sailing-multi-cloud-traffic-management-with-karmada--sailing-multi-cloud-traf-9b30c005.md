---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Customizing + Extending Kubernetes"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Zhonghu Xu", "Huawei"]
sched_url: https://kccnceu2022.sched.com/event/ytpc/sailing-multi-cloud-traffic-management-with-karmada-zhonghu-xu-huawei
youtube_search_url: https://www.youtube.com/results?search_query=Sailing+Multi+Cloud+Traffic+Management+With+Karmada+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Sailing Multi Cloud Traffic Management With Karmada - Zhonghu Xu, Huawei

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Customizing + Extending Kubernetes]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Zhonghu Xu, Huawei
- Schedule: https://kccnceu2022.sched.com/event/ytpc/sailing-multi-cloud-traffic-management-with-karmada-zhonghu-xu-huawei
- Busca YouTube: https://www.youtube.com/results?search_query=Sailing+Multi+Cloud+Traffic+Management+With+Karmada+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Sailing Multi Cloud Traffic Management With Karmada.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpc/sailing-multi-cloud-traffic-management-with-karmada-zhonghu-xu-huawei
- YouTube search: https://www.youtube.com/results?search_query=Sailing+Multi+Cloud+Traffic+Management+With+Karmada+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=rzFbxeZQHWI
- YouTube title: Sailing Multi Cloud Traffic Management With Karmada - Zhonghu Xu, Huawei
- Match score: 0.93
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/sailing-multi-cloud-traffic-management-with-karmada/rzFbxeZQHWI.txt
- Transcript chars: 17588
- Keywords: cluster, clusters, multi-cloud, commander, network, traffic, resources, second, across, policy, single, management, application, easter, provider, override, remote, kinetics

### Resumo baseado na transcript

hello everyone welcome to my presentation i feel very honored to be here today i will share about sitting marked cloud traffic management with commander first let me introduce myself i'm jonghoshui an open source engineer from hawaii previously i worked on upstream kinetics community and a call contributor in siga api machinery and since 208 i joined easter community and became the co-maintainer of easter and i'm a student committee member i like open source if you are interested please feel free to connect me in github let's first

### Excerpt da transcript

hello everyone welcome to my presentation i feel very honored to be here today i will share about sitting marked cloud traffic management with commander first let me introduce myself i'm jonghoshui an open source engineer from hawaii previously i worked on upstream kinetics community and a call contributor in siga api machinery and since 208 i joined easter community and became the co-maintainer of easter and i'm a student committee member i like open source if you are interested please feel free to connect me in github let's first look at the agenda of today today my presentation includes three most critical part the first part i will talk about the multi-cloud benefits and the disadvantages next i will talk about commander a young sensative project which handles multi-cloud workload of situation with kubernetes api it is natively suitable for multi-cloud application management the third i will talk about multi-cloud traffic management this may be the most tricky point user can face when adopting multi-cluster automatic cloud oh first let's look at the multi-cloud martie's cluster strategy is widely adopted let me do a quick explanation of my cloud my is when an individual or organization uses more than one cloud provider for the itiness the approach enables companies to better support their business technology and service needs this approach enables companions to better support their business technology and service reliability requirements while mitigating over reliance on a single cloud provider that might not accomplish all tasks effectively a multi-cloud strategy can encompass private public and hybrid class and allows business to seamlessly manage multi-profit providers and virtual infrastructure performance while achieving great efficiency as a figure indicates of the respondents report having a multi-cloud strategy it is still the de facto standard but the ways in which organizations arrive at multi-cloud vary depending on their needs and mix of providers to them most are taking a hybrid approach you can see at the figure of the respondents adopt hybrid hybrid cloud okay why we choose multicloud speaking of multi cloud benefits it is commonly compared with single cloud i listed four points here one is avoid vendor locking one of the most this is the most persuasive multi-cloud benefits it keeps organizations from being locked into one vendor or service provider a multi-cloud app approach enables business to deploy multi-specialist services instead
