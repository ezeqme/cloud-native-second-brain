---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Storage Data"]
speakers: ["Christophe Tafani-Dereeper", "Datadog", "Diego Comas", "Sourcegraph"]
sched_url: https://kccnceu2023.sched.com/event/1HyZm/mind-the-gap-bringing-together-cloud-services-and-managed-k8s-environments-christophe-tafani-dereeper-datadog-diego-comas-sourcegraph
youtube_search_url: https://www.youtube.com/results?search_query=Mind+the+Gap%21+Bringing+Together+Cloud+Services+and+Managed+K8s+Environments+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Mind the Gap! Bringing Together Cloud Services and Managed K8s Environments - Christophe Tafani-Dereeper, Datadog & Diego Comas, Sourcegraph

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Christophe Tafani-Dereeper, Datadog, Diego Comas, Sourcegraph
- Schedule: https://kccnceu2023.sched.com/event/1HyZm/mind-the-gap-bringing-together-cloud-services-and-managed-k8s-environments-christophe-tafani-dereeper-datadog-diego-comas-sourcegraph
- Busca YouTube: https://www.youtube.com/results?search_query=Mind+the+Gap%21+Bringing+Together+Cloud+Services+and+Managed+K8s+Environments+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Mind the Gap! Bringing Together Cloud Services and Managed K8s Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyZm/mind-the-gap-bringing-together-cloud-services-and-managed-k8s-environments-christophe-tafani-dereeper-datadog-diego-comas-sourcegraph
- YouTube search: https://www.youtube.com/results?search_query=Mind+the+Gap%21+Bringing+Together+Cloud+Services+and+Managed+K8s+Environments+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5luByA7hakc
- YouTube title: Mind the Gap! Bringing Together Cloud Services and Managed K8s Environments- Tafani-Dereeper & Comas
- Match score: 0.951
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/mind-the-gap-bringing-together-cloud-services-and-managed-k8s-environm/5luByA7hakc.txt
- Transcript chars: 30874
- Keywords: access, cluster, account, application, metadata, secrets, credentials, create, specific, information, permissions, default, identity, instance, secret, against, workload, running

### Resumo baseado na transcript

hello everyone Welcome to our talk and I'm just going to send myself my name is Diego Commerce I'm the head of security at sourcegraph I've been protecting Cloud native environments and kubernetes environments in many companies I love all the security that can be enabled and the cloud native projects so I would love to talk about all this here stuff up hi everyone I'm Kristoff I work at data log mostly focusing on cloud security and open source topics and yeah take it away you go thank you

### Excerpt da transcript

hello everyone Welcome to our talk and I'm just going to send myself my name is Diego Commerce I'm the head of security at sourcegraph I've been protecting Cloud native environments and kubernetes environments in many companies I love all the security that can be enabled and the cloud native projects so I would love to talk about all this here stuff up hi everyone I'm Kristoff I work at data log mostly focusing on cloud security and open source topics and yeah take it away you go thank you so today we would like to talk about common pitfalls in managed kubernetes environments and some traps that you can find yourself to get into because it's many things that can happen there just to start how many of you are working with Amazon eks okay quite a few how many of you Google gke okay and Acer oh quite a few how many of you multi-cloud well that's great thank you we'll have for all of you thank you so and at the end we're going to show you that we're releasing a tool that is going to help you to mitigate and handle some of the pitfalls and problems that we're going to show you here so stay tuned because it's going to help you definitely cool so we're going to be following the Journey of Kate today so Kate is a cloud native software engineer and she's going to build a cat classifier app so it's a very simple app you give it a picture of a cat and it gives you back what kind of cat it is so cage has an AWS account with an eks cluster already deployed and she's going to deploy her application on the crystal so she authenticates to AWS she runs the right command to get her cubeconfig and she's a bit cautious because she doesn't have any kind of access she has access denied but she's a full admin to AWS account and that's the first thing that we generally run into the first trick is that when you're on admin and AWS you don't necessarily have any kind of permissions on your Humanities cluster and this is because permissions are managed inside of the cluster not through AWS I am so this also adds a complexity that whoever creates the AWS eks cluster has invisible and immutable rights to it so if it was maybe Kate's friend Jenny who created the cluster two years ago she will still be a full admin of that but you don't see it anywhere and you cannot remove it uh so this is the default config map that you have in the eks cluster it's a config map that basically Maps AWS identities to kubernetes groups and in this case this is the default one that tells you okay I want m
