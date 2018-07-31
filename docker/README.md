## Authorization PDP - AuthzForce Docker minimal image

[Authorization PDP - AuthzForce](http://catalogue.fiware.org/enablers/authorization-pdp-authzforce) is a Reference Implementation of the Authorization PDP Generic Enabler (formerly Access Control GE).

Find detailed information of this Generic Enabler at [Fiware catalogue](http://catalogue.fiware.org/enablers/authorization-pdp-authzforce).

This image is intended to work together with [Identity Manager - Keyrock](http://catalogue.fiware.org/enablers/identity-management-keyrock) and [PEP Proxy Wilma](http://catalogue.fiware.org/enablers/pep-proxy-wilma) generic enabler; and also integrated in Bitergia's [Chanchan APP](https://github.com/Bitergia/fiware-chanchan).

## Image contents
- OpenJDK JRE 8;
- Tomcat 8;
- Authzforce Server (version matching the Docker image tag).

## Usage

This image gives you a minimal installation for testing purposes. The AuthzForce Installation and administration guide on [readthedocs.org](https://readthedocs.org/projects/authzforce-ce-fiware/versions/) (select the version matching the Docker image tag, then **AuthzForce - Installation and Administration Guide**) provides you a better approach for using it in a production environment. This installation guide also gives instructions to install from .deb package (instead of Docker), which is the recommended way for Ubuntu hosts.

Create a container using `fiware/authzforce-ce-server` image by doing (replace the first *8080* after *-p* with whatever network port you want to use on the host to access the Authzforce Server, e.g. 80; and *release-6.0.0* with the current Docker image tag that you are using):

```
docker run -d -p 8080:8080 --name <container-name> fiware/authzforce-ce-server:release-6.0.0
```

As stands in the AuthzForce Installation and administration guide on [readthedocs.org](https://readthedocs.org/projects/authzforce-ce-fiware/versions/) (select the version matching the Docker image tag, then **AuthzForce - Installation and Administration Guide**) you can:

* **Create a domain**

```
curl -s --request POST \
--header "Accept: application/xml" \
--header "Content-Type: application/xml;charset=UTF-8" \
--data '<?xml version="1.0" encoding="UTF-8"?><taz:domainProperties xmlns:taz="http://authzforce.github.io/rest-api-model/xmlns/authz/5" />' \
 http://<authzforce-container-ip>:8080/authzforce-ce/domains
```

* **Retrieve the domain ID**

```
curl -s --request GET http://<authzforce-container-ip>:8080/authzforce-ce/domains
```

* **Domain removal**

```
curl --verbose --request DELETE \
--header "Content-Type: application/xml;charset=UTF-8" \
--header "Accept: application/xml" \
http://<authzforce-container-ip>:8080/authzforce-ce/domains/<domain-id>
```

* **User and Role Management Setup && Domain Role Assignment**

These tasks are now delegated to the [Identity Manager - Keyrock](http://catalogue.fiware.org/enablers/identity-management-keyrock) enabler. Here you can find how to use the interface for that purpose: [How to manage AuthzForce in Fiware](https://www.fiware.org/devguides/handling-authorization-and-access-control-to-apis/how-to-manage-access-control-in-fiware/).

## User feedback

### Documentation

All the information regarding the Dockerfile is hosted publicly on [Github](https://github.com/authzforce/fiware/tree/master/docker).

### Issues

If you find any issue with this image, feel free to report at [Github issue tracking system](https://github.com/authzforce/fiware/issues).
