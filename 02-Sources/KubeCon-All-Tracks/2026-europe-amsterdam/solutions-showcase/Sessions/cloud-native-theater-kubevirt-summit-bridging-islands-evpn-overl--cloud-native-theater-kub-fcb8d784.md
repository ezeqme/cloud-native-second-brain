---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["Kubernetes Core"]
speakers: ["Miguel Duarte", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2EG0n/cloud-native-theater-kubevirt-summit-bridging-islands-evpn-overlays-for-multi-cluster-kubevirt-miguel-duarte-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+Bridging+Islands%3A+EVPN+Overlays+for+Multi-Cluster+KubeVirt+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | KubeVirt Summit: Bridging Islands: EVPN Overlays for Multi-Cluster KubeVirt - Miguel Duarte, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Miguel Duarte, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2EG0n/cloud-native-theater-kubevirt-summit-bridging-islands-evpn-overlays-for-multi-cluster-kubevirt-miguel-duarte-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+Bridging+Islands%3A+EVPN+Overlays+for+Multi-Cluster+KubeVirt+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | KubeVirt Summit: Bridging Islands: EVPN Overlays for Multi-Cluster KubeVirt.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0n/cloud-native-theater-kubevirt-summit-bridging-islands-evpn-overlays-for-multi-cluster-kubevirt-miguel-duarte-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+Bridging+Islands%3A+EVPN+Overlays+for+Multi-Cluster+KubeVirt+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=P0V_IiI3Qh4
- YouTube title: Cloud Native Theater | KubeVirt Summit: Bridging Islands: EVPN Overlays for Multi-C... Miguel Duarte
- Match score: 0.968
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-kubevirt-summit-bridging-islands-evpn-overlays-fo/P0V_IiI3Qh4.txt
- Transcript chars: 16720
- Keywords: cluster, address, network, running, bridge, clusters, virtual, machine, migration, router, everything, client, workloads, instance, pretty, multiple, workload, stretch

### Resumo baseado na transcript

I work for Red Hat specifically in the networking team for well downstream distribution of cubevert and well here to present to you about like uh EVPN overlays for a multicluster cube. So our agenda for today we're going to begin with the motivation like what brings us here what problem are we trying to solve with this? Now the implementation this is where things uh get a little bit trickier but we have very simple design principles here. Here we are pointing at two like ovs CNI and bridge CNI but you could use more than them uh like oven kubernetes probably cube oven we haven't checked that out but probably it could work and I'll see uh we'll see more about that in a second. So openp router this is nothing more than a router running in each of your Kubernetes nodes. it will expose networking to the Kubernetes node via a vest pair which is left dangling on the it's left uh dangling on the physical nodes and then you can just plump it in any way you want into your VMs and or containers.

### Excerpt da transcript

Uh hello everyone. My name is uh Miguel. I work for Red Hat specifically in the networking team for well downstream distribution of cubevert and well here to present to you about like uh EVPN overlays for a multicluster cube. So our agenda for today we're going to begin with the motivation like what brings us here what problem are we trying to solve with this? Then explain what goals we have, what EVPN is, what it's used for, and well, how it is implemented. Show a brief demo and finalize with some conclusions. Okay, what brings us here? First thing, some uh type of applications like legacy applications, they totally depend on being um L2 adjacent. This means how many of you have seen VMs where its ID is pretty much its IP address. I guess this is quite common in the virtualization world and it's not amazing. That means that you if you have to import or you want to migrate that VM off to a different platform, you need to bring the carry the network address with it like both MAC IP that entire thing.

That means that everybody's stuck with the same IP address. it got probably back in 2010 and that is not good. So you're stuck with having to maintain the uh network ID and IP addresses of the VMs. Another thing a reason for you to have multicluster is clearly uh resiliency. Your application will be more resilient. Uh it's actually quite common in the cloud for you to architect something for I don't know your availability zone to go down first. So that means like the entire cluster going down and have a way for that application to res keep continuing working in a different cluster. Finally, you might have hybrid cloud scenarios. So you could have part of your application in onrem and another part of your application running on different clouds somewhere. In case one of these clouds go down, it can still work. in part your on-prem data center goes down, it will still keep working. So multicluster is a thing. Now what problems do we have with that? First scalability. So what you would usually do on the virtualization world is to just plum VLANs into everything like we will solve everything with a VLAN.

Thing is that's not scalable. It like 4,094 VLANs might sound like a lot, but it clearly isn't. like uh after I don't know for multi-tenency you will not go far with 4,94 uh efficiency also like you have multiple uh clusters workloads like lots of workloads in both clusters remember uh in cube vert you have pods and containers in the same network this means that
