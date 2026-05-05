---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Service Mesh"
themes: ["Networking"]
speakers: ["Iris Ding", "Intel", "Faseela Kundattil", "Ericsson Software Technology"]
sched_url: https://kccncna2023.sched.com/event/1R2wC/flavors-of-certificates-in-service-mesh-the-whys-and-hows-iris-ding-intel-faseela-kundattil-ericsson-software-technology
youtube_search_url: https://www.youtube.com/results?search_query=Flavors+of+Certificates+in+Service+Mesh%3A+The+Whys+and+Hows%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Flavors of Certificates in Service Mesh: The Whys and Hows! - Iris Ding, Intel & Faseela Kundattil, Ericsson Software Technology

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Service Mesh]]
- Temas: [[Networking]]
- País/cidade: United States / Chicago
- Speakers: Iris Ding, Intel, Faseela Kundattil, Ericsson Software Technology
- Schedule: https://kccncna2023.sched.com/event/1R2wC/flavors-of-certificates-in-service-mesh-the-whys-and-hows-iris-ding-intel-faseela-kundattil-ericsson-software-technology
- Busca YouTube: https://www.youtube.com/results?search_query=Flavors+of+Certificates+in+Service+Mesh%3A+The+Whys+and+Hows%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Flavors of Certificates in Service Mesh: The Whys and Hows!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2wC/flavors-of-certificates-in-service-mesh-the-whys-and-hows-iris-ding-intel-faseela-kundattil-ericsson-software-technology
- YouTube search: https://www.youtube.com/results?search_query=Flavors+of+Certificates+in+Service+Mesh%3A+The+Whys+and+Hows%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1aYVoQNo3qc
- YouTube title: Flavors of Certificates in Service Mesh: The Whys and Hows! - Iris Ding & Faseela Kundattil
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/flavors-of-certificates-in-service-mesh-the-whys-and-hows/1aYVoQNo3qc.txt
- Transcript chars: 25971
- Keywords: certificate, server, gateway, option, mesh, workload, private, request, external, certificates, secret, traffic, actually, signing, security, cluster, support, scenarios

### Resumo baseado na transcript

hello everyone welcome to this session uh my name is aris Ste uh I'm A Cloud software engineer from Intel so my focus is try to accelerate and secure s smesh while unleashing the underlying Hardware capabilities um my I'm currently a East maintainer and seing in the East steering commune member uh so together with me is facila so faila would you please introduce yourself hello everyone I'm facila I work as a cloud native developer at ericon software technology uh where my primary responsibility is prioritizing the 5G

### Excerpt da transcript

hello everyone welcome to this session uh my name is aris Ste uh I'm A Cloud software engineer from Intel so my focus is try to accelerate and secure s smesh while unleashing the underlying Hardware capabilities um my I'm currently a East maintainer and seing in the East steering commune member uh so together with me is facila so faila would you please introduce yourself hello everyone I'm facila I work as a cloud native developer at ericon software technology uh where my primary responsibility is prioritizing the 5G TCO requirements in all the different open- Source communities uh I'm a steering committee member and maintainer at ISO and um recently I'm a cncf Ambassador for the latest 2023 group as well so here is a quick overview of the agenda whatever we are planning to cover today so I iris iris is a security maintainer at hiso so she will be talking about an overview of the certificates in hiso service mesh uh different types of certificates and uh the different plug-in mechanisms for the same and she will also touch upon a little bit about confidential Computing and her work related to that in Intel and after that I will uh dig a little bit deeper into the certificate revocation list and ocsp stapling support in ISO we will also talk about the different extended TLS configurations that ISO supports um and then Since U my experience is basically in the 5G Telco security so we will just talk in brief about the 5G um Telco security overview and then different traffic scenarios in the same and the different uh certificate configurations for the same as well now over to you Iris to get started thank you Fila so uh let's first take overw our Al certificate in E service mesh so as you know uh security and mutal TI are very key functions for service MH so um for most end users actually when they Landing service mesh in their in their environment the MS might be the first choice of the feature they want to utilize so to a the mut TI uh actually for each of the workload you need a certificate and a private key to do the TS communication so as showed in this picture in this green um Arrow here this is the workload certificate and also in the mesh Edge side either in the Ingress Gateway direction or the ESS Gateway Direction you need a several different uh certificate as well for example you need to do the T termination in the Ingress Direction or in the erress Declaration you also need the certificate to the TRS origination so you might also for example expose
