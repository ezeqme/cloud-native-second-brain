---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Connectivity"
themes: ["Networking"]
speakers: ["Daniel Borkmann", "Anton Protopopov", "Isovalent at Cisco"]
sched_url: https://kccncna2025.sched.com/event/27FXg/qemu-in-the-fast-lane-accelerating-kubevirt-networking-with-ebpf-daniel-borkmann-anton-protopopov-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=QEMU+in+the+Fast+Lane%3A+Accelerating+KubeVirt+Networking+With+eBPF+CNCF+KubeCon+2025
slides: []
status: parsed
---

# QEMU in the Fast Lane: Accelerating KubeVirt Networking With eBPF - Daniel Borkmann & Anton Protopopov, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Networking]]
- País/cidade: United States / Atlanta
- Speakers: Daniel Borkmann, Anton Protopopov, Isovalent at Cisco
- Schedule: https://kccncna2025.sched.com/event/27FXg/qemu-in-the-fast-lane-accelerating-kubevirt-networking-with-ebpf-daniel-borkmann-anton-protopopov-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=QEMU+in+the+Fast+Lane%3A+Accelerating+KubeVirt+Networking+With+eBPF+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre QEMU in the Fast Lane: Accelerating KubeVirt Networking With eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FXg/qemu-in-the-fast-lane-accelerating-kubevirt-networking-with-ebpf-daniel-borkmann-anton-protopopov-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=QEMU+in+the+Fast+Lane%3A+Accelerating+KubeVirt+Networking+With+eBPF+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3X0X4az_E_4
- YouTube title: QEMU in the Fast Lane: Accelerating KubeVirt Networking With... Daniel Borkmann & Anton Protopopov
- Match score: 0.888
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/qemu-in-the-fast-lane-accelerating-kubevirt-networking-with-ebpf/3X0X4az_E_4.txt
- Transcript chars: 25308
- Keywords: device, netkit, basically, kernel, actually, physical, traffic, selium, network, application, support, networking, question, devices, packet, context, driver, latency

### Resumo baseado na transcript

Hello and welcome everyone to our talk about uh QMO in the fast lane and how we accelerate cube word networking with the help of ebpf. This talk um in this project uh has been done in collaboration with my colleague Anton Yusi and myself and yeah to set the context a little bit um not too long ago the virtualization landscape has been shaking up a bit. And now you can migrate everything over um into Kubernetes um for both VM and container workloads. Um just to give you a architecture picture in terms of how the cube um networking side looks. Can we re imagine how we do the networking like the VM networking in Kubernetes? And before I go into that I want to go a little bit uh more to the fundamental side in terms of how we solved um container networking with selium to remove the the overhead there for Kubernetes ports.

### Excerpt da transcript

Hello and welcome everyone to our talk about uh QMO in the fast lane and how we accelerate cube word networking with the help of ebpf. This talk um in this project uh has been done in collaboration with my colleague Anton Yusi and myself and yeah to set the context a little bit um not too long ago the virtualization landscape has been shaking up a bit. I found this quite a interesting quote from the MIT technology review. In late 2023, a long trusted virtualization staple became the biggest open question on the enterprise IT road map. So a lot of enterprises are now rethinking whether to stick to the current um stack or whether to migrate and modernize the infrastructure potentially going into the Kubernetes space because they have containers running anyway there. And the question is are there any viable OSS solutions with help with that um strategic reset to move the VM infrastructure into into Kubernetes and we think the answer is yes that is a cube word and together with selium to help with the networking and then and throughout this talk I will detail you uh why that is in general.

So the combination of Kubernetes and cube word basically enables users to um converge their infrastructure. So you basically previously you had two stacks you had two logging solution metrics monitoring solutions one for your legacy VM platform the other one for Kubernetes. And now you can migrate everything over um into Kubernetes um for both VM and container workloads. And that helps with the overall user uh experience given it's now unified. Um just to give you a architecture picture in terms of how the cube um networking side looks. So you basically have your Kubernetes node. Cube is launching a Kubernetes pod, a launcher pod for the VM. So your regular CNI is setting up VE devices for example with one V flag in the host name space one V flag in the in the pod namespace and then Cubeword is setting up a bridge device and in a tab and then it's launching QMO KVM as a VM and it's basically connecting to that and the IP address it's getting to a DHCP where you can then manage the IPM So we had the for this talk we basically had the so-called moonshot idea.

Can we re imagine how we do the networking like the VM networking in Kubernetes? And before I go into that I want to go a little bit uh more to the fundamental side in terms of how we solved um container networking with selium to remove the the overhead there for Kubernetes ports. If you look at a standard Kubernetes um
