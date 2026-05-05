---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Sponsor Theater"
themes: ["Sponsor Theater"]
speakers: ["Kevin (Zefeng) Wang", "Huawei"]
sched_url: https://kccnceu2021.sched.com/event/igUf/sponsored-lightning-talk-beyond-federation-automating-multi-cloud-workloads-with-k8s-native-apis-kevin-zefeng-wang-huawei
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Beyond+Federation%3A+Automating+Multi-cloud+Workloads+with+K8s+Native+APIs+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Sponsored Lightning Talk: Beyond Federation: Automating Multi-cloud Workloads with K8s Native APIs - Kevin (Zefeng) Wang, Huawei

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Sponsor Theater]]
- Temas: [[Sponsor Theater]]
- País/cidade: Virtual / Virtual
- Speakers: Kevin (Zefeng) Wang, Huawei
- Schedule: https://kccnceu2021.sched.com/event/igUf/sponsored-lightning-talk-beyond-federation-automating-multi-cloud-workloads-with-k8s-native-apis-kevin-zefeng-wang-huawei
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Beyond+Federation%3A+Automating+Multi-cloud+Workloads+with+K8s+Native+APIs+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Sponsored Lightning Talk: Beyond Federation: Automating Multi-cloud Workloads with K8s Native APIs.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/igUf/sponsored-lightning-talk-beyond-federation-automating-multi-cloud-workloads-with-k8s-native-apis-kevin-zefeng-wang-huawei
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Lightning+Talk%3A+Beyond+Federation%3A+Automating+Multi-cloud+Workloads+with+K8s+Native+APIs+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=LJJoaGszBVk
- YouTube title: Sponsored Lightning Talk: Beyond Federation: Automating Multi-cloud Workloads... Kevin (Zefeng) Wang
- Match score: 0.905
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/sponsored-lightning-talk-beyond-federation-automating-multi-cloud-work/LJJoaGszBVk.txt
- Transcript chars: 3808
- Keywords: clusters, applications, provide, policy, cluster, federation, multi-cloud, native, policies, propagation, override, automating, workloads, providers, result, following, customization, including

### Resumo baseado na transcript

hello my name is kevin wong open source architect from hawaii cloud i'm streaming kubernetes and csf contributor today i want to talk about automating multi-cloud workloads with the kubernetes native apis you have probably seen this report already that 93 of enterprises have a strategy to use multiple providers the fact that kubernetes has matured over years along with the cloud market will hopefully unlock programmatic multi-cloud managing services however there are still many challenges as more and more applications running on top of kubernetes you may result in

### Excerpt da transcript

hello my name is kevin wong open source architect from hawaii cloud i'm streaming kubernetes and csf contributor today i want to talk about automating multi-cloud workloads with the kubernetes native apis you have probably seen this report already that 93 of enterprises have a strategy to use multiple providers the fact that kubernetes has matured over years along with the cloud market will hopefully unlock programmatic multi-cloud managing services however there are still many challenges as more and more applications running on top of kubernetes you may result in the following situations the first one too many clusters repeating setup due to the incompatible cluster lifecycle apis or fragmentation of yaml's lack of simplified way to do per cluster customization for applications or functionalities including resource scheduling auto scaling etc limited to the boundary of clusters and even more you may find that you're still locked in somewhere due to the gravity of foreclosure instance and data as the early participant and the doctor of kubernetes federation the major lessons we learned from previous work are as following a couple of apis embedding with application definition placement requirement and customization requirements are complicated and the api incompatibility really slowed down people's adoption one-to-one mapping of federation api and workload are redundant which result in too many fields to fill out every time we create applications and the building blocks are insufficient lack of time key solution and too many customizations resulting no standard therefore we started thinking about the new project k amarda we are targeting on providing the kubernetes native aps support with a set of extra policies to provide the dual actual mode aja remote disaster recovery for different scenarios and to avoid to avoid the vendor locking besides uh some integration with mainstream providers we also provide automatic allocation and migration across clusters and also we provide things like cluster affinity multi-cluster splitting and rebalancing kind of advanced multi-cluster scheduling features clear model is able also able to provide location agnostic the api endpoint and access for clusters no matter in public cloud on-prem or on-age especially this project is jointly initiated by the end users from internet finance manufacturing and televised industries here's the architectural overview of the kmart project here model runs its own api server to provide temp
