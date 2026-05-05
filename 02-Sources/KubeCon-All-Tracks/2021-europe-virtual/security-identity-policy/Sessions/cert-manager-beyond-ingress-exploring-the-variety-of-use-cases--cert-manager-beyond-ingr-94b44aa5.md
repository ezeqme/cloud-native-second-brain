---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Security + Identity + Policy"
themes: ["Security", "Networking"]
speakers: ["Matthew Bates", "Jetstack"]
sched_url: https://kccnceu2021.sched.com/event/iE58/cert-manager-beyond-ingress-exploring-the-variety-of-use-cases-matthew-bates-jetstack
youtube_search_url: https://www.youtube.com/results?search_query=Cert-Manager+Beyond+Ingress+%E2%80%93+Exploring+the+Variety+of+Use+Cases+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cert-Manager Beyond Ingress – Exploring the Variety of Use Cases - Matthew Bates, Jetstack

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Networking]]
- País/cidade: Virtual / Virtual
- Speakers: Matthew Bates, Jetstack
- Schedule: https://kccnceu2021.sched.com/event/iE58/cert-manager-beyond-ingress-exploring-the-variety-of-use-cases-matthew-bates-jetstack
- Busca YouTube: https://www.youtube.com/results?search_query=Cert-Manager+Beyond+Ingress+%E2%80%93+Exploring+the+Variety+of+Use+Cases+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cert-Manager Beyond Ingress – Exploring the Variety of Use Cases.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE58/cert-manager-beyond-ingress-exploring-the-variety-of-use-cases-matthew-bates-jetstack
- YouTube search: https://www.youtube.com/results?search_query=Cert-Manager+Beyond+Ingress+%E2%80%93+Exploring+the+Variety+of+Use+Cases+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wEW2kVKxgss
- YouTube title: Cert-Manager Beyond Ingress – Exploring the Variety of Use Cases - Matthew Bates, Jetstack
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cert-manager-beyond-ingress-exploring-the-variety-of-use-cases/wEW2kVKxgss.txt
- Transcript chars: 24712
- Keywords: certificate, manager, certificates, resources, cluster, private, request, ingress, effectively, certain, actually, driver, secure, secret, number, mesh, issuer, course

### Resumo baseado na transcript

hi everybody thanks for joining my talk it's great to be able to talk to you about the cert manager project this year it's virtual but hopefully in the not too distant future we'll all be able to meet up again soon and meet in person i'm going to talk to you today about all the various ways in which you can use set manager beyond ingress i'm matt bates i'm from jet stack with the original creators of the project and together with now 280 contributors in the community

### Excerpt da transcript

hi everybody thanks for joining my talk it's great to be able to talk to you about the cert manager project this year it's virtual but hopefully in the not too distant future we'll all be able to meet up again soon and meet in person i'm going to talk to you today about all the various ways in which you can use set manager beyond ingress i'm matt bates i'm from jet stack with the original creators of the project and together with now 280 contributors in the community we've got set manager to where it is today sub manager is effectively a kubernetes add-on or extension but it extends the kubernetes api and adds support for certificates and certificate authorities it means that you can manage x509 tls certificates that's the complete life cycle the issuance and renewal and use those certificates in your applications it has wide adoption and lots of contribution from the community and as of last year we donated the project to the cncf so it's now part of the sandbox it's got integration with a variety of different public and private pki providers both in the core of the project but also a so-called external issuers and we're going to look at that in the talk today briefly how does certain manager work as i said search manager is an extension or an add-on it provides a number of additional resources so called custom resources crds and provides them to the key on top of the kubernetes api these represent certificates and certificate authorities we can refer to that as an issuer this provides first-class support for those in the kubernetes api and you get all of the advantages of being able to manage those resources declaratively much like you manage pods and deployments set manager has a controller that manages the lifecycle of those resources and importantly is able to provide the automation of those certificates automating the fetching of those certificates and importantly the renewal of those as well is most commonly used to secure ingresses and you can see here it's really quick and easy to add a tls certificate to an ingress it's important by adding in this case the annotation which references where you want the certificate to be obtained from so in this case it references the let's encrypt staging issuer that i have in my cluster and it also requires you to specify the secret name there as well so the secret will store the certificates obtained from let's encrypt in my ingress so really really simple how does this work under the hood well set manager watc
