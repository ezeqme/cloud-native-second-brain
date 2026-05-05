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
themes: ["AI ML", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Angel M De Miguel Meana", "VMware", "Francisco Cabrera", "Microsoft"]
sched_url: https://kccnceu2024.sched.com/event/1YeMp/strategies-for-efficient-llm-deployments-in-any-cluster-angel-m-de-miguel-meana-vmware-francisco-cabrera-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Strategies+for+Efficient+LLM+Deployments+in+Any+Cluster+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Strategies for Efficient LLM Deployments in Any Cluster - Angel M De Miguel Meana, VMware & Francisco Cabrera, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Unclassified]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: France / Paris
- Speakers: Angel M De Miguel Meana, VMware, Francisco Cabrera, Microsoft
- Schedule: https://kccnceu2024.sched.com/event/1YeMp/strategies-for-efficient-llm-deployments-in-any-cluster-angel-m-de-miguel-meana-vmware-francisco-cabrera-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Strategies+for+Efficient+LLM+Deployments+in+Any+Cluster+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Strategies for Efficient LLM Deployments in Any Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeMp/strategies-for-efficient-llm-deployments-in-any-cluster-angel-m-de-miguel-meana-vmware-francisco-cabrera-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Strategies+for+Efficient+LLM+Deployments+in+Any+Cluster+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PRzxq3ZuIdQ
- YouTube title: Strategies for Efficient LLM Deployments in Any Cluster -Angel M De Miguel Meana & Francisco Cabrera
- Match score: 0.804
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/strategies-for-efficient-llm-deployments-in-any-cluster/PRzxq3ZuIdQ.txt
- Transcript chars: 29552
- Keywords: models, actually, pretty, container, cluster, gpu, layers, energy, specific, access, billion, already, simple, download, little, source, course, probably

### Resumo baseado na transcript

thank you very much for attending our session today we are going to talk about strategies for efficient LM deployments in any cluster my name is sel and I'm part of the AI and advanc services team in the in bracom and today I'm here with Francisco hey my name is Francisco Caba I'm a senior technical program manager at the Asher agent platform team so just to set a little bit expectations for this talk the goal is that we will learn different strategies to run operate and improve

### Excerpt da transcript

thank you very much for attending our session today we are going to talk about strategies for efficient LM deployments in any cluster my name is sel and I'm part of the AI and advanc services team in the in bracom and today I'm here with Francisco hey my name is Francisco Caba I'm a senior technical program manager at the Asher agent platform team so just to set a little bit expectations for this talk the goal is that we will learn different strategies to run operate and improve models while working on their on um specific use cases setting also the appropriate infrastructure so we can run them in different environments not only in a big cluster and a huge Cloud but also in a small deployments like on premise inside stores on anywhere in which you want to run them for that we will talk about local catching oci for models GP usage and you may be familiar with this terms after like being here at cuom for for one day also so we will focus on a small and medium kubernetes deployments nothing about like AI service provider or Mega cluster for distributed training but more something that you can deploy in your own premise clusters but before starting with the strategies and discussing a little bit more about that the first thing you may ask yourself if is why you would like why you consider to deploy L lamps that are already a huge offering outside with a lot of really good models that you can just access them via API so you you don't need to host install and manage those ones but there are 13 good reasons to to deploy them and manage the first thing is that you have more control and flexibility if you start using one of those Services most likely you will have access to the models that the propietary models that they offer but you won't have the ability to experiment with new models go as small try new things and that may impact also the cost because now you are tied to the cost of the service that you that you choose also because any company can actually access to those services and you can access get um and use those models but the real difference between any of the companies that we are here is the data that you have but maybe certain regulations like if you work on a government or by other reason because you don't want to move your data to the services you want to keep it private so deploying a LMS locally may give you access to that data that otherwise you can not use and based on that you can also find in the models there is a huge offering on the open so
