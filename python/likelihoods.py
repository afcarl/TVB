import numpy as np
from scipy.special import gamma, digamma

class student_t():
    def __init__(self):
        self._set_params(np.ones(2))
    def _set_params(self, p):
        self.nu, self.lamb = p
        #compute some constants so that they don't appear in a loop
        self._pdf_const = gamma((self.nu + 1)/2.) / gamma(self.nu/2.) * np.sqrt(self.lamb/(self.nu*np.pi) )
        self._dnu_const = 0.5*digamma((self.nu + 1.)/2.) - 0.5*digamma(self.nu/2.) - 0.5/self.nu
    def _get_params(self):
        return np.array([self.nu, self.lamb])
    def _get_param_names(self):
        return ['nu', 'lambda']
    def pdf(self, x, Y):
        x2 = np.square(x-Y)
        return self._pdf_const * np.power(1 + self.lamb*x2/self.nu, -(self.nu + 1.)/2.)
    def dlnpdf_dtheta(self, x, Y):
        x2 = np.square(x-Y)
        dnu = self._dnu_const - 0.5*np.log(1. + self.lamb*x2/self.nu) + 0.5*(self.nu + 1.)*(self.lamb*x2/self.nu**2)/(1. + self.lamb*x2/self.nu)
        dlamb =  0.5/self.lamb - 0.5*(self.nu + 1.)*(x2/self.nu/(1.+self.lamb*x2/self.nu))
        return np.vstack((dnu, dlamb))
