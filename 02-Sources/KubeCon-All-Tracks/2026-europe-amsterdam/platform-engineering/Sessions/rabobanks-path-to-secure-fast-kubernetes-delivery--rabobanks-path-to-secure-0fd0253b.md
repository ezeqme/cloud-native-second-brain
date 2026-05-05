---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Security", "Platform Engineering", "GitOps Delivery", "Kubernetes Core"]
speakers: ["Beatrice Forslund", "Koshin Verberne", "Rabobank"]
sched_url: https://kccnceu2026.sched.com/event/2CW4N/rabobanks-path-to-secure-fast-kubernetes-delivery-beatrice-forslund-koshin-verberne-rabobank
youtube_search_url: https://www.youtube.com/results?search_query=Rabobank%E2%80%99s+Path+to+Secure%2C+Fast+Kubernetes+Delivery+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Rabobank’s Path to Secure, Fast Kubernetes Delivery - Beatrice Forslund & Koshin Verberne, Rabobank

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Security]], [[Platform Engineering]], [[GitOps Delivery]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Beatrice Forslund, Koshin Verberne, Rabobank
- Schedule: https://kccnceu2026.sched.com/event/2CW4N/rabobanks-path-to-secure-fast-kubernetes-delivery-beatrice-forslund-koshin-verberne-rabobank
- Busca YouTube: https://www.youtube.com/results?search_query=Rabobank%E2%80%99s+Path+to+Secure%2C+Fast+Kubernetes+Delivery+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Rabobank’s Path to Secure, Fast Kubernetes Delivery.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW4N/rabobanks-path-to-secure-fast-kubernetes-delivery-beatrice-forslund-koshin-verberne-rabobank
- YouTube search: https://www.youtube.com/results?search_query=Rabobank%E2%80%99s+Path+to+Secure%2C+Fast+Kubernetes+Delivery+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cznwYOK3TtY
- YouTube title: Rabobank’s Path to Secure, Fast Kubernetes Delivery - Beatrice Forslund & Koshin Verberne, Rabobank
- Match score: 0.775
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/rabobanks-path-to-secure-fast-kubernetes-delivery/cznwYOK3TtY.txt
- Transcript chars: 22054
- Keywords: platform, cluster, tenants, clusters, security, tenant, started, create, secure, running, having, within, across, production, giving, access, policies, argo

### Resumo baseado na transcript

Uh thank you for attending our presentation about uh how we deliver uh Kubernetes uh in a secure and uh well very fast uh delivery at the at the Rabo Bank. Uh managing and delivering Kubernetes clusters to uh to tenants at the bank. own Kubernetes clusters especially in cloud uh for some uh understanding of what the uh landscape looks like. So for on Azure we have about 147 or close to 150 uh Azure Kubernetes uh service clusters uh running and 473 uh Azure container uh apps uh which is underneath also yeah managed Kubernetes. uh second for the uh second provider we're also running on AWS EKS so elastic kubernetes service with there a little bit over 40 uh EKS clusters running there and uh we also have still our on premise running uh where we have about roughly operate on Kubernetes clusters there but throughout the years as we started up maturing our platform offering we've begun to approach these teams to tell them to migrate and uh also get uh backing from architecture to say like yeah we need to have more

### Excerpt da transcript

Good afternoon everyone. Uh thank you for attending our presentation about uh how we deliver uh Kubernetes uh in a secure and uh well very fast uh delivery at the at the Rabo Bank. Uh I am Kosher Fern. >> Uh my name is Petris. >> Yes. So we both work at the container platform team at the Rabo Bank. Uh managing and delivering Kubernetes clusters to uh to tenants at the bank. So today we will tell you about how what our journey was like to uh delivering Kubernetes uh the decisions and challenges we faced at uh making uh the Kubernetes experience secure and compliant according to the bank's uh regulations and standards and uh how we overcame these challenges and what advice or giveaways we can share with you the audience. And we know it is probably one of the last presentations some of you will attend. So we try to keep it also a bit light-hearted. Uh little bit about ourselves. So I am a uh platform engineer who previously worked at the AWS platform team for uh about five years. So actually Kubernetes is uh relatively new for me.

I started last year with it and uh I've been learning quite a lot uh going through it and uh also from this event. >> All right. Yeah. I am I started working in open shift um now working with AKS and I'm also a cubestronaut and this is our f first uh talk at cubecon. >> Yes. So uh told you about uh Kubernetes and what we do with Kubernetes. So maybe for the uh international audience who don't know about Raab Bank, uh we're a Dutch bank uh serving close to 9 million uh customers and uh we also uh operate internationally to uh well fund and finance farmers all over the globe. Uh well and how we do this we have a lot of uh of our infrastructure uh hosted across uh three uh landing zones uh at the bank and uh in recent years also a lot of developers have really enjoyed building and operating their own Kubernetes clusters especially in cloud uh for some uh understanding of what the uh landscape looks like. So for on Azure we have about 147 or close to 150 uh Azure Kubernetes uh service clusters uh running and 473 uh Azure container uh apps uh which is underneath also yeah managed Kubernetes.

uh second for the uh second provider we're also running on AWS EKS so elastic kubernetes service with there a little bit over 40 uh EKS clusters running there and uh we also have still our on premise running uh where we have about roughly about 12 open shift clusters and on open shift we started from the beginning with a uh container platform team
