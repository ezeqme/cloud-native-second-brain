---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Governance + Risk + Compliance (GRC)"
themes: ["Kubernetes Core", "Community Governance"]
speakers: ["Tyler Lisowski", "Kodie Glosser IBM"]
sched_url: https://kccnceu2023.sched.com/event/1HyVi/implementing-an-auditable-access-control-strategy-using-cluster-certificate-authority-rotation-tyler-lisowski-kodie-glosser-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Implementing+an+Auditable+Access+Control+Strategy+Using+Cluster+Certificate+Authority+Rotation+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Implementing an Auditable Access Control Strategy Using Cluster Certificate Authority Rotation - Tyler Lisowski & Kodie Glosser IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Governance + Risk + Compliance (GRC)]]
- Temas: [[Kubernetes Core]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Tyler Lisowski, Kodie Glosser IBM
- Schedule: https://kccnceu2023.sched.com/event/1HyVi/implementing-an-auditable-access-control-strategy-using-cluster-certificate-authority-rotation-tyler-lisowski-kodie-glosser-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Implementing+an+Auditable+Access+Control+Strategy+Using+Cluster+Certificate+Authority+Rotation+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Implementing an Auditable Access Control Strategy Using Cluster Certificate Authority Rotation.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVi/implementing-an-auditable-access-control-strategy-using-cluster-certificate-authority-rotation-tyler-lisowski-kodie-glosser-ibm
- YouTube search: https://www.youtube.com/results?search_query=Implementing+an+Auditable+Access+Control+Strategy+Using+Cluster+Certificate+Authority+Rotation+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H1ndetiaN0g
- YouTube title: Implementing an Auditable Access Control Strategy Using Cluster... - Tyler Lisowski & Kodie Glosser
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/implementing-an-auditable-access-control-strategy-using-cluster-certif/H1ndetiaN0g.txt
- Transcript chars: 22804
- Keywords: certificates, cluster, components, server, actually, process, certificate, bundle, updated, administrator, question, across, typically, revocation, associated, update, excellent, access

### Resumo baseado na transcript

hey everyone we're super grateful for y'all making the time today to um for um for y'all making the time to listen to us talk my name's Tyler lisowski this is Cody glosser and we're extremely excited to talk to you all today about implementing an access control system based off of CA rotation I'm going to turn it over to Cody to um to to um to kick us off so go ahead awesome thanks Tyler for the introduction so let's take a look at a typical kubernetes cluster

### Excerpt da transcript

hey everyone we're super grateful for y'all making the time today to um for um for y'all making the time to listen to us talk my name's Tyler lisowski this is Cody glosser and we're extremely excited to talk to you all today about implementing an access control system based off of CA rotation I'm going to turn it over to Cody to um to to um to kick us off so go ahead awesome thanks Tyler for the introduction so let's take a look at a typical kubernetes cluster deployment well there's one CA across the cluster DCA issues all their certificate for the cluster components the certificate grants the components the ability to do specific actions like a kubernetes kublet's ability to create no data but let's imagine we have a kubernetes cluster and someone has access to your ca whether it's an administrator that's left the organization that had admin access or malicious attacker that gained access to the cluster and the ca or their security controls in your company or organization that require CA certificates to be rotated how do you prove that their access was revoked without the ability to rotate the CA and a client Circ does not expire what is your strategy and what do you do without CA rotation they basically own your cluster one strategy is to delete the cluster and recreate it to get a new ca which will require you to migrate your applications not an ideal solution we need a way to provoke the certificates with a zero downtime fashion of the cluster and our applications we're going to talk today about this CA rotation process that allow you to meet all these objectives we're going to solve in a way to not take the workload offline and rotate the zero dial time of the cluster of the applications I'm going to hand it over to Tyler talk about this process thank you Cody so now let's picture us collectively in this room as an organization that operates kubernetes clusters for our business as part of this organization Cody and I are going to be the administrator team as part of the administrator team we will be responsible for all operations associated with our kubernetes clusters in order to perform those operations Cody and I are going to be granted admin certificates to the cluster that will allow us to do operations like corded and drain nodes view utilization across cluster components debug software-defined overlays Etc everything's going to be going great with our operations for a year business applications continue to get on board in that drive business v
