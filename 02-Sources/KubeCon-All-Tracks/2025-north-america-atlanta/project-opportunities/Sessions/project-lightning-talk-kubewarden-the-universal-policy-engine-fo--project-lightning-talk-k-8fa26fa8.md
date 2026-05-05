---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["Security", "Kubernetes Core"]
speakers: []
sched_url: https://kccncna2025.sched.com/event/27d4H/project-lightning-talk-kubewarden-the-universal-policy-engine-for-kubernetes
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubewarden%3A+The+Universal+Policy+Engine+For+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Kubewarden: The Universal Policy Engine For Kubernetes

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: N/A
- Schedule: https://kccncna2025.sched.com/event/27d4H/project-lightning-talk-kubewarden-the-universal-policy-engine-for-kubernetes
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubewarden%3A+The+Universal+Policy+Engine+For+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Kubewarden: The Universal Policy Engine For Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4H/project-lightning-talk-kubewarden-the-universal-policy-engine-for-kubernetes
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Kubewarden%3A+The+Universal+Policy+Engine+For+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Uy-PpGOMEcU
- YouTube title: Project Lightning Talk: Kubewarden: The Universal Policy Engine For Kubernetes
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-kubewarden-the-universal-policy-engine-for-kube/Uy-PpGOMEcU.txt
- Transcript chars: 3308
- Keywords: policies, policy, universal, needed, engine, enforce, cluster, everywhere, developers, kuborton, configurations, within, looked, maintainers, support, consumers, operators, ability

### Resumo baseado na transcript

Um, I'm going to be talking about Kuborton, the universal policy engine for Kubernetes. By definition, a policy is a writing where a by a contract of insurance is made. case for us to use this within the kubernetes space with that from there we looked at taking a gitops approach with our policies but to make it universal we needed the concept of policies everywhere. use cases as well that are outside of cluster because we needed to meet policies universally everywhere and we understand that sometimes things can't run in Kubernetes and And that's okay.

### Excerpt da transcript

All right, so they're guess they're going to let me go. Hello, welcome. My name is Robert. Um, I'm going to be talking about Kuborton, the universal policy engine for Kubernetes. Um, I'm a CNF ambassador. I'm contributor. Um, and I'm one of the maintainers for the project helm. And yes, I know there's a lot of red. We can talk about it later. All right. So, what is a policy? By definition, a policy is a writing where a by a contract of insurance is made. But in our world, policies are configurations that manage other configurations or runtime behaviors. So that being said, let's establish what a policy engine is. And this is a tool that's designed to enforce specific rules and guidance guidelines of the creation configurations of the management of objects within a Kubernetes cluster. So this is the slide I'm going to spend most of my time on here. What is a universal policy engine? Well, to be universal, you want and need to be able to go and be everywhere and be everything and that's not possible. But what we did was we looked at our users first and we needed to meet their needs of policy users and we needed to do that by leveraging pre-existing policies whether those are RIO Kyverno or even the policies and artifact hub that Kuborton has created already and we recommend that our users do such a thing as use what we built before instead of redesigning the wheel.

But if you have your own RIGO policies, we want to support those as well. We looked at our personas such as consumers, developers, operators, and integrator developers etc. Our consumers are the people who the policies enforce upon when they're using a C a cluster. Our developers are developers who are creating such policies and our operators are the ones who operate those policies with it. To do this we needed to support multiple languages and we do that from net to go to rust and all of this is compiled into small binaries for our users using wom I know it's a web assembly but it was a perfect use case for us to use this within the kubernetes space with that from there we looked at taking a gitops approach with our policies but to make it universal we needed the concept of policies everywhere. So policies everywhere for us was supporting a bigger scope with policies and you see on my diagram here we have policies for our cluster where cub currently kubort and sits but we have the ability to enforce policies within VMs and on our edge use cases as well that are outside of cluster because we need
