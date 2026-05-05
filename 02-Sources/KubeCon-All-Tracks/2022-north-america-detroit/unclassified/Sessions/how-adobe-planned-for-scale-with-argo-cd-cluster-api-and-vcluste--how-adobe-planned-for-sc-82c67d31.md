---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["GitOps Delivery", "Kubernetes Core", "SRE Reliability"]
speakers: ["Joseph Sandoval", "Adobe", "Dan Garfield", "Codefresh"]
sched_url: https://kccncna2022.sched.com/event/182Dx/how-adobe-planned-for-scale-with-argo-cd-cluster-api-and-vcluster-joseph-sandoval-adobe-dan-garfield-codefresh
youtube_search_url: https://www.youtube.com/results?search_query=How+Adobe+Planned+For+Scale+With+Argo+CD%2C+Cluster+API%2C+And+VCluster+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How Adobe Planned For Scale With Argo CD, Cluster API, And VCluster - Joseph Sandoval, Adobe & Dan Garfield, Codefresh

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[GitOps Delivery]], [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Joseph Sandoval, Adobe, Dan Garfield, Codefresh
- Schedule: https://kccncna2022.sched.com/event/182Dx/how-adobe-planned-for-scale-with-argo-cd-cluster-api-and-vcluster-joseph-sandoval-adobe-dan-garfield-codefresh
- Busca YouTube: https://www.youtube.com/results?search_query=How+Adobe+Planned+For+Scale+With+Argo+CD%2C+Cluster+API%2C+And+VCluster+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How Adobe Planned For Scale With Argo CD, Cluster API, And VCluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Dx/how-adobe-planned-for-scale-with-argo-cd-cluster-api-and-vcluster-joseph-sandoval-adobe-dan-garfield-codefresh
- YouTube search: https://www.youtube.com/results?search_query=How+Adobe+Planned+For+Scale+With+Argo+CD%2C+Cluster+API%2C+And+VCluster+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p8BluR5WT5w
- YouTube title: How Adobe Planned For Scale With Argo CD, Cluster API, And VCluster - Joseph Sandoval & Dan Garfield
- Match score: 0.898
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-adobe-planned-for-scale-with-argo-cd-cluster-api-and-vcluster/p8BluR5WT5w.txt
- Transcript chars: 36713
- Keywords: argo, cluster, actually, clusters, applications, running, approach, application, trying, source, familiar, started, looking, workflow, reconciliation, multiple, instances, support

### Resumo baseado na transcript

welcome everybody thank you for joining us you are the Friday Cloud you the you're the Friday crowd you stuck it out you didn't go to the airport so give yourself a round of applause already great job yes nights yeah uh so uh we're going to talk about how Adobe planned for scale with Argo CD cluster API and V cluster Joseph you want to introduce yourself yeah I'm Joseph senal I am with Adobe which is just in the title I am now a product manager for our feature of Argo CD to help you scale um it's basically a stateful set that is going to divide up and Shard how we manage all of the Clusters and the reconciliation um for the scale that we're looking at over probably the next year you're probably going to have some reconciliation challenges so to solve this it's good to use an app of apps pattern uh where you basically split up the application into multiple components and this has other advantages because you can do things like say this

### Excerpt da transcript

welcome everybody thank you for joining us you are the Friday Cloud you the you're the Friday crowd you stuck it out you didn't go to the airport so give yourself a round of applause already great job yes nights yeah uh so uh we're going to talk about how Adobe planned for scale with Argo CD cluster API and V cluster Joseph you want to introduce yourself yeah I'm Joseph senal I am with Adobe which is just in the title I am now a product manager for our Dev experience Group which really means that I'm still working with the underlying kubernetes infrastructure and then in this alternate life I get to hang out with kubernetes Sig release team been part of like five release Cycles Branch release manager associate still trying to retain it because that's one of the things I've highly value yeah and uh I'm Dan Garfield I am the co-founder and chief open source officer of codefresh H and I also uh feel like I live a dual life because I'm also an Argo maintainer and then I uh helped start the uh gitops working group and open gitops as the geop standards that are uh cncf project that uh I've been very pleased to see a lot of pickup on at coupon and L and lots of people's slides so we're going to talk about Adobe and how you're scaling yeah so you know a lot of us are familiar with the brand we know all the cool creative things that we do but that's just like one aspect of what we do at Adobe you know we have itics to areas we are very big in Ai and ML and improving our products with these types of developments and there's also other areas like marketing and so there's quite a bit of a portfolio that adobe has and so if you hit up any of the talks this week um You probably there's a couple people here who have been speaking about what's been happening there um but you may have heard the name ethos but what ethos is it's it's the cloud native platform if you're going to do anything there that's the spot it's going to happen at and this platform has existed for for about 5 years and so a lot of change has happened a lot of developments the interesting things about it is that we scaled and so the cluster counts and grown um it's Dynamic we have about 230 clusters roughly 18,000 compute nodes 1.8 paby of memory and about 500,000 CPUs along with that project is growing I think the last count was 2.3 million and along with it we were a company of about 26,000 and you can imagine a lot our developers so so the great thing is we're scaling uh change is happening there and
