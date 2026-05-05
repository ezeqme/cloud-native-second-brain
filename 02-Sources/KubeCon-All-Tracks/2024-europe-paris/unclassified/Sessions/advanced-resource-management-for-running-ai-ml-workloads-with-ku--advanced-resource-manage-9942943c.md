---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Unclassified"
themes: ["AI ML"]
speakers: ["Michał Woźniak", "Google", "Yuki Iwai", "CyberAgent", "Inc."]
sched_url: https://kccnceu2024.sched.com/event/1YeLj/advanced-resource-management-for-running-aiml-workloads-with-kueue-michal-wozniak-google-yuki-iwai-cyberagent-inc
youtube_search_url: https://www.youtube.com/results?search_query=Advanced+Resource+Management+for+Running+AI%2FML+Workloads+with+Kueue+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Advanced Resource Management for Running AI/ML Workloads with Kueue - Michał Woźniak, Google & Yuki Iwai, CyberAgent, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]]
- País/cidade: France / Paris
- Speakers: Michał Woźniak, Google, Yuki Iwai, CyberAgent, Inc.
- Schedule: https://kccnceu2024.sched.com/event/1YeLj/advanced-resource-management-for-running-aiml-workloads-with-kueue-michal-wozniak-google-yuki-iwai-cyberagent-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Advanced+Resource+Management+for+Running+AI%2FML+Workloads+with+Kueue+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Advanced Resource Management for Running AI/ML Workloads with Kueue.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeLj/advanced-resource-management-for-running-aiml-workloads-with-kueue-michal-wozniak-google-yuki-iwai-cyberagent-inc
- YouTube search: https://www.youtube.com/results?search_query=Advanced+Resource+Management+for+Running+AI%2FML+Workloads+with+Kueue+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6k_8Go3u8Qk
- YouTube title: Advanced Resource Management for Running AI/ML Workloads with Kueue - Michał Woźniak, Yuki Iwai
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/advanced-resource-management-for-running-ai-ml-workloads-with-kueue/6k_8Go3u8Qk.txt
- Transcript chars: 27490
- Keywords: cluster, admission, resource, resources, feature, provisioning, machines, request, management, running, workloads, support, gpu, second, clusters, important, autoscaler, workload

### Resumo baseado na transcript

okay I think we are um ready to start um so let me introduce uh myself uh I'm mik I'm a software engineer uh working for Google and today I will co-present with uh Yuki who is a software engineer at uh cyber agent and uh we are going to talk about Q um which is the project that we are maintainers of um and we will show and demonstrate capabilities of Q to build uh a platform for running AIML workloads uh and in particular focusing on the capabilities

### Excerpt da transcript

okay I think we are um ready to start um so let me introduce uh myself uh I'm mik I'm a software engineer uh working for Google and today I will co-present with uh Yuki who is a software engineer at uh cyber agent and uh we are going to talk about Q um which is the project that we are maintainers of um and we will show and demonstrate capabilities of Q to build uh a platform for running AIML workloads uh and in particular focusing on the capabilities for qu uh Resource Management so let me start by introducing what uh is Q so Q is a job level scheduler and as such is its responsibility is to determine when to start or stop a job so it operates a one level higher of abstraction than uh Cube schedular that operates on pods so with Q we uh delay uh po creation actually until the job is started and this is very important because with this capability we are able to offload the uh API server and Cube Schuler uh another important characteristic of Q is that we have the goal of supporting uh All or Nothing semantic so for machine learning jobs uh it is very important that all pods are running at the same time uh so as you can imagine with limited resources if two large jobs start at the same time they could deadlock and could not run all the pots so this is one of the important goals for Q um and of course with Q we support quter management so we support quter management both at the team level that lets you specify the quotas per team um because maybe they have different priorities uh we also support specifying qu for different resource uh types like different models of gpus and we also give you control of preferences for different um machines like how they are provisioned is it on demand or reservations that you have some discounts on because maybe there are different prices depending on how the uh nodes come to be so how does q achieve its goals so the main design principle of Q is actually very simple uh we want to be Cloud native and what this means so this means that for example we don't need to have any external database so uh everything lives in inside etcd that is managed by Cube API server also we are compatible and coexist nicely with all uh cor kubernetes components such as cluster autoscaler Cube schedular or job controller so none of the components is forked or replaced uh when working with q and of course sometimes we encounter gaps in the core components um but then we have like policy for pushing the required uh enhancements Upstream so one success
