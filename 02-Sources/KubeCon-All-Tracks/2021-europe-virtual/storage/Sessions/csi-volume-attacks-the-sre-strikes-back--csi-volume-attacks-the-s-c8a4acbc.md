---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Storage"
themes: ["Storage Data", "SRE Reliability"]
speakers: ["Hendrik Land", "NetApp"]
sched_url: https://kccnceu2021.sched.com/event/iE4P/csi-volume-attacks-the-sre-strikes-back-hendrik-land-netapp
youtube_search_url: https://www.youtube.com/results?search_query=CSI+Volume+Attacks+%E2%80%93+The+SRE+Strikes+Back+CNCF+KubeCon+2021
slides: []
status: parsed
---

# CSI Volume Attacks – The SRE Strikes Back - Hendrik Land, NetApp

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Storage]]
- Temas: [[Storage Data]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Hendrik Land, NetApp
- Schedule: https://kccnceu2021.sched.com/event/iE4P/csi-volume-attacks-the-sre-strikes-back-hendrik-land-netapp
- Busca YouTube: https://www.youtube.com/results?search_query=CSI+Volume+Attacks+%E2%80%93+The+SRE+Strikes+Back+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre CSI Volume Attacks – The SRE Strikes Back.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE4P/csi-volume-attacks-the-sre-strikes-back-hendrik-land-netapp
- YouTube search: https://www.youtube.com/results?search_query=CSI+Volume+Attacks+%E2%80%93+The+SRE+Strikes+Back+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=A9IwOHGt7gM
- YouTube title: CSI Volume Attacks – The SRE Strikes Back - Hendrik Land, NetApp
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/csi-volume-attacks-the-sre-strikes-back/A9IwOHGt7gM.txt
- Transcript chars: 20004
- Keywords: storage, volume, access, namespace, security, permissions, cluster, control, create, policy, prevent, specific, inline, driver, resource, server, attacker, specify

### Resumo baseado na transcript

hello welcome everyone to another kitchen session i hope you enjoy the event in this talk i'll show you the different ways to attack storage volumes that are dynamically provisioned with a csi drive and how you as an sae can prevent my name is hendrick i'm a solution architect at netapp and i help our customers with storage and data management solutions for kubernetes both in public cloud as well as in their own data centers and one of the questions i get a lot is around csi the that access the same data you cannot have each pot apply different permissions to the volume one pot would effectively lock out the other part also if the fs type is not specified in the storage class kubernetes will not apply those permissions assuming that it is a file system that does not support this so in those cases kubernetes does not apply the fs group permission even if you set them in a security context there is a recent addition in the csi spec that allows drivers to specify most linux systems are configured to try version 4 first and then fall back to version 3 if necessary but you can also enforce a specific version with mount options specified in your storage class as all mounting of volumes is handled by your csi you to configure export policies that limit access to an nfs export to specific appear addresses or hostnames it acts a little bit like a firewall just for nfs as the nodes...

### Excerpt da transcript

hello welcome everyone to another kitchen session i hope you enjoy the event in this talk i'll show you the different ways to attack storage volumes that are dynamically provisioned with a csi drive and how you as an sae can prevent my name is hendrick i'm a solution architect at netapp and i help our customers with storage and data management solutions for kubernetes both in public cloud as well as in their own data centers and one of the questions i get a lot is around csi the container storage interface which is really nice because it orchestrates the equation of volumes snapshots and clones but the question is how does it protect my data from unauthorized access in this session i will show you what is available in kubernetes and how to enable and configure it we will have a live q a at the end so if you have any questions please let me know you can also find me on the cubecon slack if you'd like to discuss anything so just as a very brief recap how does dynamic storage provisioning with csi work for the purpose of this session i'm going to focus on the part level of course in a real world environment you would have to stay for set if it is a stateful workload or a deployment or replica set i'm leaving these details out that they are not relevant for this topic i'm also focusing on dynamic storage provisioning with the container storage interface so with csi along with the pot the user requests another kubernetes resource the persistent volume plane or short pvc that volume claim references the storage class the storage class allows to offer multiple service levels for storage in our cluster so the user can decide what type of storage service he needs by using a specific storage class for the volume thing and this is where the container storage interface comes into play the storage class has a csi provisioner and this is how you can integrate different storage solutions into kubernetes each solution has its own provisioner that takes care of everything that's required for that specific solution but for the user or application all of these complexities are stacked away you just create a pvc that references a storage class everything else happens automatically by whatever csi provisioner is running in your cluster the provisioner creates an actual storage volume depending on the solution you're using that can be a software-defined storage running in your kubernetes or an external storage array of storage server the volume from a storage solution is then r
