---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Reliability + Operational Continuity"
themes: ["AI ML", "Storage Data", "Runtime Containers", "Kubernetes Core", "SRE Reliability"]
speakers: ["Laurent Bernaille", "Eric Mountain", "Datadog"]
sched_url: https://kccncna2022.sched.com/event/182Iz/building-container-images-in-kubernetes-its-been-a-journey-laurent-bernaille-eric-mountain-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Building+Container+Images+In+Kubernetes%3A+It%E2%80%99s+Been+a+Journey%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Building Container Images In Kubernetes: It’s Been a Journey! - Laurent Bernaille & Eric Mountain, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Reliability + Operational Continuity]]
- Temas: [[AI ML]], [[Storage Data]], [[Runtime Containers]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Laurent Bernaille, Eric Mountain, Datadog
- Schedule: https://kccncna2022.sched.com/event/182Iz/building-container-images-in-kubernetes-its-been-a-journey-laurent-bernaille-eric-mountain-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Container+Images+In+Kubernetes%3A+It%E2%80%99s+Been+a+Journey%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Building Container Images In Kubernetes: It’s Been a Journey!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Iz/building-container-images-in-kubernetes-its-been-a-journey-laurent-bernaille-eric-mountain-datadog
- YouTube search: https://www.youtube.com/results?search_query=Building+Container+Images+In+Kubernetes%3A+It%E2%80%99s+Been+a+Journey%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=01eLHZDp6bs
- YouTube title: Building Container Images In Kubernetes: It’s Been a Journey! - Laurent Bernaille & Eric Mountain
- Match score: 0.864
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/building-container-images-in-kubernetes-its-been-a-journey/01eLHZDp6bs.txt
- Transcript chars: 31430
- Keywords: docker, images, actually, running, extended, process, directory, builds, inside, namespace, attribute, read.go, pretty, username, consistent, overlay, container, interesting

### Resumo baseado na transcript

hello everyone my name is Lauren bernai and I'm here with Eric and I mean we're very happy to be here today it's our first coupon in person since 2019 in North America so that's that's great to to be here with you So today we're going to to discuss our migration of uh the way we build container images to kubernetes and as you you will see it was a bit eventful and it got pretty interesting so before we start we both work for datadoc so we have

### Excerpt da transcript

hello everyone my name is Lauren bernai and I'm here with Eric and I mean we're very happy to be here today it's our first coupon in person since 2019 in North America so that's that's great to to be here with you So today we're going to to discuss our migration of uh the way we build container images to kubernetes and as you you will see it was a bit eventful and it got pretty interesting so before we start we both work for datadoc so we have a few numbers and of about datadag on the left hand side of the slide what matters is with our an obserability company and and we do a lot of things in the obserability space but today we're not going to talk about dialogue the product we're going to talk about data dogs infrastructure because we both work on the dialogue infrastructure teams so we essentially work on the kubernetes environment which is why we're going to talk about building containers in kubernetes and as you can see with the numbers I mean we have tens of thousands of nodes dozens of clusters and and with this come a lot of challenges around many things but in particular building container images so before we dive into an interesting issue let's do a quick overview of how we build things at datadog so quite a while back I'd say it's like up to four or five years ago we were using this very simple setup to build our applications so we had gitlab Runners pulling jobs from gitlab and using Docker machine to provision Edibles instances a running job on them so pretty standard pretty simple when we started our migration to kubernetes we needed to in addition to building applications we also needed to build container images and if you're familiar with the way we build Docker images it usually means having access to the docker demon which basically means being root on the instance where where you run so that's why we couldn't reuse the runners we were using for applications because these Runners will be used and there was no way we could run a workload which will end up being root on the machine because it was running Docker commands so we ended up having other Runners which were just General Admissions running Docker doing one job and when the job was done they were just being killed and replaced by new ones that was working fine until sometime when the company had grown a bit and we were having many more Engineers many more builds every day and Docker machine was starting to hit limits we're hitting API rate limits with the AWS API and it was starting t
