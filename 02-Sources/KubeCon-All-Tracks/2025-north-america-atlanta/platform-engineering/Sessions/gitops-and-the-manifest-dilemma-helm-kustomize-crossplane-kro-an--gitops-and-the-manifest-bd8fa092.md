---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "GitOps Delivery"]
speakers: ["Dag Bjerre Andersen", "Egmont"]
sched_url: https://kccncna2025.sched.com/event/27Fe4/gitops-and-the-manifest-dilemma-helm-kustomize-crossplane-kro-and-beyond-dag-bjerre-andersen-egmont
youtube_search_url: https://www.youtube.com/results?search_query=GitOps+and+the+Manifest+Dilemma%3A+Helm%2C+Kustomize%2C+Crossplane%2C+Kro%2C+and+Beyond+CNCF+KubeCon+2025
slides: []
status: parsed
---

# GitOps and the Manifest Dilemma: Helm, Kustomize, Crossplane, Kro, and Beyond - Dag Bjerre Andersen, Egmont

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[GitOps Delivery]]
- País/cidade: United States / Atlanta
- Speakers: Dag Bjerre Andersen, Egmont
- Schedule: https://kccncna2025.sched.com/event/27Fe4/gitops-and-the-manifest-dilemma-helm-kustomize-crossplane-kro-and-beyond-dag-bjerre-andersen-egmont
- Busca YouTube: https://www.youtube.com/results?search_query=GitOps+and+the+Manifest+Dilemma%3A+Helm%2C+Kustomize%2C+Crossplane%2C+Kro%2C+and+Beyond+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre GitOps and the Manifest Dilemma: Helm, Kustomize, Crossplane, Kro, and Beyond.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fe4/gitops-and-the-manifest-dilemma-helm-kustomize-crossplane-kro-and-beyond-dag-bjerre-andersen-egmont
- YouTube search: https://www.youtube.com/results?search_query=GitOps+and+the+Manifest+Dilemma%3A+Helm%2C+Kustomize%2C+Crossplane%2C+Kro%2C+and+Beyond+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Tmiyf78sC24
- YouTube title: GitOps and the Manifest Dilemma: Helm, Kustomize, Crossplane, Kro, and Beyond - Dag Bjerre Andersen
- Match score: 0.958
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/gitops-and-the-manifest-dilemma-helm-kustomize-crossplane-kro-and-beyo/Tmiyf78sC24.txt
- Transcript chars: 33872
- Keywords: rendering, actually, resources, cluster, crossplane, argo, operator, templating, inside, manifest, githubs, incluster, custom, simple, failing, flux, template, change

### Resumo baseado na transcript

And since you have chosen to attend this talk, it's probably because you have noticed that there are so many different templating tools out there and new ones get released all the time and they go in different directions and you don't know how they fit into our current tool stack and how they work with GitHubs. And when we build the Kubernetes clusters, one of the first things we do is that we pick a GitOps tool, either Argo C or Flux. It's like a support entity that uh helps the other businesses and uh one of the things we do is that we build Kubernetes clusters and we built them for all these other companies and provisions uh software to them and applications and so on I'm referring to crossplane compositions just to be precise here which is their templating engine for generating Kubernetes manifests. And then we have the in-cluster rendering tools which are Kubernetes operators. It's something like crow or crossplane or cubella something that needs kubernetes in order to work.

### Excerpt da transcript

Hi everyone. So this talk is called GitOps and the manifest dilemma. And since you have chosen to attend this talk, it's probably because you have noticed that there are so many different templating tools out there and new ones get released all the time and they go in different directions and you don't know how they fit into our current tool stack and how they work with GitHubs. So this is some of the things we will be discussing today. And when we build the Kubernetes clusters, one of the first things we do is that we pick a GitOps tool, either Argo C or Flux. And then we pick one or two different templating tools to use for our manifests. And whenever I say templating tool, I'm basically referring to any kind of tooling that takes some kind of template in. And then we have some values that we plug into this template in order to generate our manifest. That's the very basic model we're working with here today. And the reason I'm here talking about this is because I recently had this discussion with one of my colleagues.

We needed to figure out what is the best templating solution for our company because my name is Doc and I work in a platform engineering team inside Eggmmont and I work a lot with our uh with the GitOps and Kubernetes and that kind of stuff and Eggmmont that's the largest largest media company in Northern Europe and we have 140 different companies in all shapes and sizes related to media and publishing and that kind of stuff. And the way we're organized is that we have something called Eggman IT and this is where I work. It's like a support entity that uh helps the other businesses and uh one of the things we do is that we build Kubernetes clusters and we built them for all these other companies and provisions uh software to them and applications and so on and we're using Argo CD to do this entire thing and also the developers deploy their applications through this instance. So now the question is what is the best templating solution for our case and as you know there are so many different tools out there and sometimes you can combine them you can chain them together and there it feels like there's endless possibilities here but and I've highlighted 10 of them here on the screen but you can probably think of 10 others that you would have liked to have added instead but instead of going into a detailed comparison between any of these tools um because first of all that would take way too long and secondly whatever I was going to say it's pro
