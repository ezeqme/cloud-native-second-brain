---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Andrew Harding", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV6J/bridging-the-great-divide-spiffespire-for-cross-cluster-authentication-andrew-harding-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Bridging+the+Great+Divide%3A+SPIFFE%2FSPIRE+for+Cross-Cluster+Authentication+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Bridging the Great Divide: SPIFFE/SPIRE for Cross-Cluster Authentication - Andrew Harding, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Andrew Harding, VMware
- Schedule: https://kccncna2021.sched.com/event/lV6J/bridging-the-great-divide-spiffespire-for-cross-cluster-authentication-andrew-harding-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Bridging+the+Great+Divide%3A+SPIFFE%2FSPIRE+for+Cross-Cluster+Authentication+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Bridging the Great Divide: SPIFFE/SPIRE for Cross-Cluster Authentication.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV6J/bridging-the-great-divide-spiffespire-for-cross-cluster-authentication-andrew-harding-vmware
- YouTube search: https://www.youtube.com/results?search_query=Bridging+the+Great+Divide%3A+SPIFFE%2FSPIRE+for+Cross-Cluster+Authentication+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=sjKNsnEYmiU
- YouTube title: Bridging the Great Divide: SPIFFE/SPIRE for Cross-Cluster Authentication - Andrew Harding, VMware
- Match score: 0.946
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/bridging-the-great-divide-spiffe-spire-for-cross-cluster-authenticatio/sjKNsnEYmiU.txt
- Transcript chars: 26976
- Keywords: server, workload, cluster, spiffy, identity, bundle, client, domain, little, credentials, workloads, called, source, inside, running, federation, endpoint, request

### Resumo baseado na transcript

[Applause] it's good to see you all it's good to be here uh together in person with our virtual attendees as well um my name is andrew harding i'm a spiffy spire maintainer i've been involved in those projects for the last uh three and a half years or so um i'm a staff engineer at vmware where i'm allowed to continue that work and work on it full time which is which is fantastic it's awesome um real quick before we get in today all these celebrations and and

### Excerpt da transcript

[Applause] it's good to see you all it's good to be here uh together in person with our virtual attendees as well um my name is andrew harding i'm a spiffy spire maintainer i've been involved in those projects for the last uh three and a half years or so um i'm a staff engineer at vmware where i'm allowed to continue that work and work on it full time which is which is fantastic it's awesome um real quick before we get in today all these celebrations and and and uh good times everybody i threw my back out so i won't be doing any break dancing today and if you see me like tilting to one side maybe some can run up and kind of like you know tilt me back up into the upright position um anyway moving on so we have a real quick like we got a lot to get through today so our agenda is fairly short but each of these sections is going to be meaty we're going to go over our problem statement make sure we're all on the same page we're going to do a very quick hopefully just a few minute refresher of spiffy inspire to kind of set the stage for the kubernetes controller work that we're doing and to demonstrate accomplishing cross-cluster authentication using spiffy inspire in this kubernetes controller work so real quick our problem statement you know we've we're all very familiar i think with with this this sort of setup we've got multiple kubernetes clusters we got workloads running within those clusters the uh intra communication store within kubernetes you know there's there are things that work there and that people have done to communicate between workloads within the same cluster when you start talking about workloads between clusters then the authentication story gets a little more complicated and there are solutions out there with various pros and cons today we're going to talk about solving it with spiffy and spire so what is spiffy it's the secure production identity framework for everyone it is essentially a set of specifications that are all geared around how do you get a workload a cryptographic identity that it can use to authenticate with other workloads and how do you get the public key material around so that you know receiving parties of these verifiable identity documents can you know um verify the signatures and verify the authenticity of those documents and get your authentication so at the heart of spiffy is something called the spiffy id this is your username for your service your workload this is your your identity uh it's a uri very basic uh it
